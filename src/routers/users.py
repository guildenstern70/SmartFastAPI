"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

fake_users_db = [
    {"id": 1, "username": "john_doe", "email": "jonhdoe@smart.com", "person_id": 1},
    {"id": 2, "username": "jane_smith", "email": "janesmith@smart.com", "person_id": 2},
    {"id": 3, "username": "alice_johnson", "email": "alicejohnson@smart.com", "person_id": 3},
]

@router.get("/")
async def read_users():
    return fake_users_db