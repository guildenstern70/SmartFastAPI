"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025-26
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

from src.services.user_service import UserService

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

user_service = UserService()

@router.get("/")
async def read_users():
    return user_service.get_all_users()