"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/persons",
    tags=["persons"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

fake_persons_db = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
    {"id": 3, "name": "Alice Johnson", "age": 28},
]

@router.get("/")
async def read_persons():
    return fake_persons_db