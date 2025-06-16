"""
    Smart FastAPI

    RESTful API with FastAPI and Jinja2

    Copyright (c) Alessio Saltarin, 2025
    This software is licensed under BSD License
    See LICENSE

"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.routers import users, persons

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(persons.router)

templates = Jinja2Templates("templates")

#
# Home page
#
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return  templates.TemplateResponse(name="index.html.jinja",
                                       request={"request": request},
                                       context={"version": "1.0.0"})


