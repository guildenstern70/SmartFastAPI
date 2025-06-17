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


class User(BaseModel):
    id: int
    username: str
    email: str
    person_id: int

    class Config:
        from_attributes = True  # Enable ORM mode for compatibility with ORMs like SQLAlchemy

class UserDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    person_id = Column(Integer)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
