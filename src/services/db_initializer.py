"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

import logging

from src.services.db_alchemy import DbAlchemy


class DBInitializer:
    """
    Class to initialize the database.
    """

    def __init__(self, alchemy: DbAlchemy):
        self.alchemy = alchemy
        self.logger = logging.getLogger(__name__)
        self.logger.info("- Setting SQLAlchemy database (SQLite file)")

    def initialize(self):
        """
        Initialize the database by creating all tables.
        """
        from src.models.base import Base
        Base.metadata.create_all(self.alchemy.engine)
        self.logger.info("- Database schema initialized successfully.")

    def populate(self):
        """
        Populate the database with initial data.
        """
        from src.models.person import PersonDB
        from src.models.user import UserDB
        from sqlalchemy.orm import Session

        # If the database is NOT empty, skip population
        with Session(self.alchemy.engine) as session:
            if session.query(PersonDB).count() > 0:
                self.logger.info("- Database already populated, skipping population.")
                return

        persons = [
            {"id": 1, "name": "John", "surname": "Doe", "age": 30},
            {"id": 2, "name": "Jane", "surname": "Smith", "age": 25},
            {"id": 3, "name": "Alice", "surname": "Johnson", "age": 28},
        ]

        users = [
            {"id": 1, "username": "john_doe", "email": "jonhdoe@smart.com", "person_id": 1},
            {"id": 2, "username": "jane_smith", "email": "janesmith@smart.com", "person_id": 2},
            {"id": 3, "username": "alice_johnson", "email": "alicejohnson@smart.com", "person_id": 3},
        ]

        with Session(self.alchemy.engine) as session:
            self.logger.info("- Populating database with initial data...")
            # Create persons
            session.add_all([PersonDB(**person) for person in persons])
            session.commit()

            # Create users
            session.add_all( [UserDB(**user) for user in users])
            session.commit()