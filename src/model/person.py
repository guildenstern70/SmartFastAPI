"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    surname: str
    age: int

    class Config:
        from_attributes = True  # Enable ORM mode for compatibility with ORMs like SQLAlchemy