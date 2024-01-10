from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from Final_Demo.app.config.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"
    email = Column(String(50), primary_key=True, index=True)
    password = Column(String(200))
    name = Column(String(250), nullable=True)
    surname = Column(String(100), nullable=True)
    # role = Column(String(50))
    # register_date = Column(DateTime, default=func.now())
    register_date= Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
