from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'todooos'
    id = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, index=True)