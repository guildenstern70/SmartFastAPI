"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025-26
    This software is licensed under BSD License
    See LICENSE

"""
import atexit
import logging

from src.services.db_alchemy import DbAlchemy
from src.models.user import UserDB, User


class UserService:

    def __init__(self):
        self.session = DbAlchemy().get_session()
        self.logger = logging.getLogger(__name__)
        self.logger.info("- UserService initialized with database session")
        atexit.register(self.close)

    def get_all_users(self):
        """
        Retrieve all users from the database.
        """
        users = self.session.query(UserDB).all()
        self.logger.info(f"- Retrieved {len(users)} users from the database")
        return users

    def get_user_by_id(self, user_id):
        """
        Retrieve a user by ID from the database.
        """
        user = self.session.query(UserDB).filter(UserDB.id == user_id).first()
        if user:
            self.logger.info(f"- Retrieved user with ID {user_id}")
        else:
            self.logger.warning(f"- User with ID {user_id} not found")
        return user

    def close(self):
        """
        Close the database session.
        """
        self.session.close()
        self.logger.info("- Closed database session")
