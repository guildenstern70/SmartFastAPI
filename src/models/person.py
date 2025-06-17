"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from src.models.base import Base


class Person(BaseModel):
    id: int
    name: str
    surname: str
    age: int

    class Config:
        from_attributes = True # Enable ORM mode for compatibility with ORMs like SQLAlchemy

class PersonDB(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    def __repr__(self) -> str:
        return f"<Person(id={self.id}, name={self.name}, surname={self.surname}, age={self.age})>"