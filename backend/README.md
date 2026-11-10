# B2B SaaS Backend Starter (FastAPI + SQLModel)

> **Design Objective**: Govern AI coding with strict API contracts, standard pagination, 3-layer architecture, audit timestamps, and automated Swagger documentation.

## Quick Start

```bash
# Activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies in editable mode
uv pip install -e .

# Start development server with auto-reload
python run.py
```

- 📖 Interactive Swagger API Docs: `http://localhost:8000/docs`
- 📖 Alternative ReDoc: `http://localhost:8000/redoc`
- 💡 Rebuild schemas & clean seed data: `python run.py --reset-db`

## Architecture

- `app/api/v1/`: HTTP Routers & API contract envelopes (`ApiResponse`).
- `app/core/`: Configuration, database engines, security, and tenant isolation middleware.
- `app/models/`: SQLModel entities and Pydantic DTOs (`BaseModel` with audit fields).
- `app/services/`: Pure business logic and database transaction orchestration.
- `scripts/`: Maintenance scripts (e.g. `reset_db.py`).
