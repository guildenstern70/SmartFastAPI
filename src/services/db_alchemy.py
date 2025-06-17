"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""
from sqlalchemy import create_engine


class DbAlchemy:
    """
    Class to handle database operations using SQLAlchemy.
    """

    def __init__(self):
        self.engine = create_engine(
            "sqlite:///db/database.db", connect_args={"autocommit": False}
        )

    def get_engine(self):
        """
        Get the SQLAlchemy engine.
        """
        return self.engine

    def get_session(self):
        """
        Create a new SQLAlchemy session.
        """
        from sqlalchemy.orm import sessionmaker
        session = sessionmaker(bind=self.engine)
        return session()