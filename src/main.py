"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine

from src.services.db_alchemy import DbAlchemy
from src.services.db_initializer import DBInitializer
from src.routers import users, persons

VERSION = "0.1.0"

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s      %(message)s",
)
logger.info("Welcome to Smart FastAPI v%s", VERSION)
logger.info("- Starting Smart FastAPI")

# FastAPI application instance
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Controllers
app.include_router(users.router)
app.include_router(persons.router)

# HTML template configuration
logger.info("- Setting up Jinja2 templates")
templates = Jinja2Templates("templates")

# Database configuration (in-memory SQLite)
logger.info("- Setting SQLAlchemy database (SQLite file)")
# Initialize the database
db_alchemy = DbAlchemy()
db_initializer = DBInitializer(db_alchemy)
db_initializer.initialize()
db_initializer.populate()


#
# Home page
#
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return  templates.TemplateResponse(name="index.html.jinja",
                                       request={"request": request},
                                       context={"version": VERSION})


