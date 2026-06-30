# AGENTS.md — SmartFastAPI

FastAPI + SQLAlchemy + Jinja2 RESTful template. Python 3.10+, BSD licensed.

## Dev Workflow

```bash
# Install dependencies
pip install -r requirements.txt

# Run in development mode (auto-reload)
PYTHONPATH=. fastapi dev src/main.py

# Run in production mode
PYTHONPATH=. fastapi run src/main.py
```

**`PYTHONPATH=.` is required** — all imports use the `src.*` package prefix (e.g. `from src.models.person import Person`), so the project root must be on the path.

Interactive API docs: `http://127.0.0.1:8000/docs` (Swagger UI) or `/redoc`.

## Architecture Overview

```
src/
  main.py              # App factory: wires FastAPI, routers, templates, DB init
  models/
    base.py            # SQLAlchemy DeclarativeBase (shared by all ORM models)
    person.py          # Person (Pydantic DTO) + PersonDB (SQLAlchemy ORM)
    user.py            # User (Pydantic DTO) + UserDB (SQLAlchemy ORM)
  services/
    db_alchemy.py      # DbAlchemy: engine + session factory (SQLite file at db/database.db)
    db_initializer.py  # DBInitializer: creates schema + seeds initial data on startup
    person_service.py  # PersonService: full CRUD via a long-lived SQLAlchemy session
    user_service.py    # UserService: read-only queries via a long-lived SQLAlchemy session
  routers/
    persons.py         # /api/persons — full CRUD, uses PersonService
    users.py           # /api/users  — read-only, uses UserService
templates/
  index.html.jinja     # Jinja2 home page template
static/                # CSS and images mounted at /static
db/
  database.db          # SQLite database file (auto-created on first run)
```

## Key Patterns

### Dual-class model convention
Every entity has **two classes in the same file**:
- `PersonDB(Base)` — SQLAlchemy ORM model (table mapping, uses `Column`)
- `Person(BaseModel)` — Pydantic DTO (used in router signatures and `response_model`); has `Config.from_attributes = True` to support ORM → Pydantic coercion

### Service layer instantiation
Services are instantiated **at module import time** (not via dependency injection):
```python
# src/routers/persons.py
person_service = PersonService()  # module-level singleton
```
`PersonService` and `UserService` each open a single SQLAlchemy session and register `atexit` to close it.

### Database initialisation flow
`main.py` → `DBInitializer(db_alchemy).initialize()` → `Base.metadata.create_all(engine)` → then `.populate()` seeds rows only if the `persons` table is empty.

### Static files & templates
Static assets are served from `static/` (mounted at `/static`). HTML responses use Jinja2 templates stored in `templates/` with the `.html.jinja` extension.

## Dependencies
| Package | Version | Role |
|---|---|---|
| `fastapi[standard]` | 0.138.0 | Web framework + Uvicorn server |
| `SQLAlchemy` | ~2.0.41 | ORM + SQLite engine |
| Pydantic | bundled with FastAPI | DTO validation |

