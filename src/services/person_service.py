"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""
import atexit
import logging

from src.services.db_alchemy import DbAlchemy
from src.models.person import PersonDB, Person


class PersonService:

    def __init__(self):
        self.session = DbAlchemy().get_session()
        self.logger = logging.getLogger(__name__)
        self.logger.info("- PersonService initialized with database session")
        atexit.register(self.close)

    def get_all_persons(self):
        """
        Retrieve all persons from the database.
        """
        persons = self.session.query(PersonDB).all()
        self.logger.info(f"- Retrieved {len(persons)} persons from the database")
        return persons

    def get_person_by_id(self, person_id):
        """
        Retrieve a person by ID from the database.
        """
        person = self.session.query(PersonDB).filter(PersonDB.id == person_id).first()
        if person:
            self.logger.info(f"- Retrieved person with ID {person_id}")
        else:
            self.logger.warning(f"- Person with ID {person_id} not found")
        return person

    def create_person(self, person: Person):
        """
        Create a new person in the database.
        """
        person_data = person.model_dump()
        new_person = PersonDB(**person_data)
        self.session.add(new_person)
        self.session.commit()
        self.logger.info(f"- Created new person with ID {new_person.id}")
        return new_person

    def update_person(self, person_id, person: Person):
        """
        Update an existing person in the database.
        """
        person_db = self.session.query(PersonDB).filter(PersonDB.id == person_id).first()
        if person_db:
            person_put_data = person.model_dump()
            for key, value in person_put_data.items():
                setattr(person_db, key, value)
            self.session.commit()
            self.logger.info(f"- Updated person with ID {person_id}")
            return person
        else:
            self.logger.warning(f"- Person with ID {person_id} not found for update")
            return None

    def delete_person(self, person_id):
        """
        Delete a person from the database.
        """
        person = self.session.query(PersonDB).filter(PersonDB.id == person_id).first()
        if person:
            self.session.delete(person)
            self.session.commit()
            self.logger.info(f"- Deleted person with ID {person_id}")
            return True
        else:
            self.logger.warning(f"- Person with ID {person_id} not found for deletion")
            return False

    def close(self):
        """
        Close the database session.
        """
        self.session.close()
        self.logger.info("- Closed database session")
