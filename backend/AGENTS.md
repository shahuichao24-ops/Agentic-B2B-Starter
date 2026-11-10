# Backend Agent Specification (`backend/AGENTS.md`)

> **Objective**: Restrict AI backend code generation to strict 3-tier patterns, standard response envelopes, pagination, soft-deletes, and tenant isolation base classes.

## 1. Architectural Rules

- **Layer 1: Models (`app/models/`)**
  - Define both database table entities (`table=True`) and DTOs (Create, Update, Read).
  - All database models must inherit `app.models.base.BaseModel` (`id`, `created_at`, `updated_at`, `is_deleted`, `tenant_id`).
  - State machines must inherit `(str, Enum)`.
- **Layer 2: Services (`app/services/`)**
  - All database transactions and query logic belong strictly in services.
  - Query filters must enforce `is_deleted == False`.
  - Forbid hard deletion; use `is_deleted = True`.
- **Layer 3: API Routers (`app/api/v1/endpoints/`)**
  - Enforce typed inputs (`data: SchemaCreate`) and typed outputs (`response_model=ApiResponse[SchemaRead]`).
  - All returns must wrap `success_response(data=...)` or `error_response(...)`.
  - Never return bare Python dictionaries.

## 2. Pagination Standard

- Parameters: `page: int = Query(1, ge=1)` and `page_size: int = Query(20, ge=1, le=100)`.
- Output: `PaginatedData.create(items=..., total=..., page=..., page_size=...)`.

## 3. Database Maintenance

- Rebuild all schemas and seed mock data: `python run.py --reset-db`.
