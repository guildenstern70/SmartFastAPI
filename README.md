# SmartFastAPI

SmartFastAPI is a Python template designed to simplify the development of FastAPI applications. 
It provides a set of tools and utilities that enhance the functionality of FastAPI, making it easier to build 
robust and scalable RESTful applications.

SmartFastAPI is built on top of the most modern Python libraries, including SQLAlchemy and Pydantic.

## Setup

### 1. Prerequisites
Ensure you have Python 3.10 or higher installed on your system.

### 2. Create and Activate a Virtual Environment
To keep dependencies isolated, create and activate a Python virtual environment:

```bash
# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows (Command Prompt):
.venv\Scripts\activate.bat

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install all required libraries, including FastAPI v0.138.0 and SQLAlchemy, from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Run

To run the application in Development Mode (which includes auto-reloading when source files change), execute:

```bash
PYTHONPATH=. fastapi dev src/main.py
```

To run the application in Production Mode, execute:

```bash
PYTHONPATH=. fastapi run src/main.py
```

Once started, you can access:
- **Web App Home Page**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Documentation (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
