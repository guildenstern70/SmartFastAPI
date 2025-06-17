"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

from src.models.user import UserDB
from src.services.db_alchemy import DbAlchemy

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users():
    return DbAlchemy().get_session().query(UserDB).all()