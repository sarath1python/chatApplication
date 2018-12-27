import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# User model used for authentication
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    user_name = Column(String(50))
    password = Column(String(120))
    last_login = Column(DateTime)
    created_date = Column(DateTime, default=datetime.datetime.now())
    token = relationship('token', back_populates = 'user')


# Token model - storing token while userlogin
class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    token = Column(String(40))
    user_id = Column(Integer , ForeignKey('user.id'))
