"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

from src.models.person import Person, PersonDB
from src.services.db_alchemy import DbAlchemy

router = APIRouter(
    prefix="/api/persons",
    tags=["persons"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_persons():
    return DbAlchemy().get_session().query(PersonDB).all()