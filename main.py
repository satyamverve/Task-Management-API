import sys

sys.path.append("..")

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from Final_Demo.app.models.db_models import Base
from Final_Demo.app.config.database import engine
from Final_Demo.app.modules.users.routes import router as user_router
from app.modules.login.authorize import router as login_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(login_router)


@app.get("/")
def read_root():
    return {"message": "This is the root path"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
