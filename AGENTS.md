# B2B SaaS Full-Stack Agent Specification (AGENTS.md)

> **Core Philosophy**:
> 1. **Frontend Complies with Apple HIG**: Deference (content-first), Clarity (legible typography), Depth (Inset Grouped flat cards with subtle shadows). Avoid unnecessary secondary labels and descriptions; let the layout do the explaining.
> 2. **Backend Enforces Strict Contracts**: FastAPI + SQLModel with strict 3-tier separation, unified response envelopes, standard pagination, soft-deletes, and tenant isolation base classes.
> 3. **Deterministic Engineering Suppresses AI Hallucinations**: Strictly forbid manual hex colors, custom raw HTML controls, bare dictionaries in responses, and unintercepted physical database deletes.

---

## 1. Frontend Standards (`frontend/`)

- **Tech Stack**: React 19 + Vite + Tailwind CSS v4 + `shadcn/ui` + TanStack Router / Table + Lucide Icons.
- **Visual & Layout Constraints**:
  - System canvas color is unified to `bg-background` (Apple System Gray 6). Content must be wrapped inside `<Card className="rounded-xl border shadow-sm">`.
  - All UI elements must be imported directly from `@/components/ui/` (Button, Card, Table, Badge, Sheet, Dialog, Select, Input).
  - Status badges use muted pastel tones: `pending` (zinc), `approved` (emerald), `revision` (amber), `rejected` (rose).
  - **Identity & Header Consolidation**: User profile and sign-out must be consolidated in the top header's `<ProfileDropdown />`; sidebar footer remains completely clean with no redundant user strips; debug floating drawer is disabled by default.
  - **Sidebar Navigation**: Tier-1 category titles are 14px semibold (`text-sm font-semibold`) with category icons, collapsed by default except active groups. Tier-2 navigation items are also 14px (`text-sm`), connected via a delicate left tree rail, highlighting as `bg-primary/10 text-primary font-semibold` pills without clumsy grey rectangles.
  - **Minimalist Page Layout & Compact Toolbar**: Forbid redundant page-level large headers and explanatory subheaders (breadcrumbs are self-explanatory). Forbid bulky filter cards above tables; all search and action controls must be consolidated into a compact Toolbar (`h-8` controls stream) on top of the list Card, search left-aligned, global buttons right-aligned.
  - **Pagination & Centered Dialog Standards**: All data tables must mount `<DataPagination />`. All detail drilldowns, rosters, and forms must use centered `<Dialog>` modals, not intrusive right-sliding `<Sheet>` drawers.
  - **Text-Only Row Actions & De-Manualization**: Forbid lonely square icon-only buttons in table rows (e.g. naked pencil/trash buttons). Use explicit, self-explanatory text buttons (*"Edit"*, *"Delete"*). Completely remove `<DialogDescription>` noise; dialog titles and layouts are self-explanatory.
  - **Centered Table Alignment**: Except for hierarchical tree columns and long descriptive text columns (which remain left-aligned for baseline readability), all other attribute columns (status, category, count, badge, switches) and action columns must have both header (`<TableHead>`) and cell content (`<TableCell>`) centered (`text-center` and `justify-center`).
  - **Viewport Protection**: Table cards must wrap tables with `<div className="overflow-x-auto">` with a minimum width, ensuring action columns are never truncated under narrow split screens. `DialogContent` must include `max-h-[88vh] overflow-y-auto` scroll protection.
  - **Universal Risk Confirmation**: Strictly forbid browser native `window.confirm()`. All destructive actions must trigger `<ConfirmDialog />`.
  - **Icon Standard**: The sole icon library is **Lucide Icons** (`lucide-react`, standard spec `h-4 w-4`). Forbid third-party icon packs or inline raw SVGs.
  - **Anti-Hallucination Guard**: Tailwind v4 has no config file; TanStack Router must use `createFileRoute`. Forbid legacy react-router syntax.

---

## 2. Backend Standards (`backend/`)

- **Tech Stack**: Python 3.12 + FastAPI + SQLModel + Pydantic v2 + SQLite (local dev) / PostgreSQL (production).
- **Architectural Constraints**:
  - Strict 3-tier boundary: `models/` (schemas & DTOs), `services/` (business logic & transactions), `api/v1/` (routes & response packaging).
  - All endpoint returns must wrap `success_response(data=...)` or `error_response(message=..., code=...)`.
  - List endpoints must accept `page` and `page_size` and return `PaginatedData`.
  - All business models must inherit `app.models.base.BaseModel` (inheriting `id`, `created_at`, `updated_at`, `is_deleted`, `tenant_id`).
  - **Tenant-Scoped Query Filter**: Database layer hooks automatically inject current `tenant_id` and `is_deleted == False` into SELECT queries. Unique constraints on business entities must be scoped by `(field, tenant_id)`.
  - **Role-Based Access Control (RBAC)**: Support `UserRole (admin | reviewer | operator)`; sensitive routes must be guarded by `dependencies=[Depends(require_roles([...]))]`.
  - Forbid hard deletes: always use `is_deleted = True`. State machines must inherit `str, Enum`.
  - **One-Click Reset**: Run `python run.py --reset-db` to rebuild fresh schemas and seed data instantly.

---

## 3. Product Manager Direct Prompts (PM Direct Prompts)

When a PM or user provides natural-language feature requests, execute immediately following these conventions:
1. **Full-Stack Feature**: *"Add a [Supplier Qualification Review] module, including paginated table, review status state machine (pending/approved/revision/rejected), and dialog for revision notes. Enable soft-delete."*
   - AI first creates Model, Service, and API in `backend/`;
   - Then creates Inset Card table and Dialog modal in `frontend/`.
2. **Frontend-Only View**: *"Add a [Compliance Metrics] page fetching stats from backend and rendering soft pastel metric cards."*
3. **Backend-Only Service**: *"Add a batch Excel import endpoint for suppliers with credit code regex validation."*
