"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import APIRouter

from src.models.person import Person
from src.services.person_service import PersonService

router = APIRouter(
    prefix="/api/persons",
    tags=["persons"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

person_service = PersonService()

@router.get("/")
async def read_persons():
    return person_service.get_all_persons()

@router.get("/{person_id}", response_model=Person)
async def read_person(person_id: int):
    person = person_service.get_person_by_id(person_id)
    if person:
        return person
    else:
        return {"error": "Person not found"}

@router.post("/", response_model=Person)
async def create_person(person: Person):
    new_person = person_service.create_person(person)
    return new_person

@router.put("/{person_id}", response_model=Person)
async def update_person(person_id: int, person: Person):
    updated_person = person_service.update_person(person_id, person)
    if updated_person:
        return updated_person
    else:
        return {"error": "Person not found"}