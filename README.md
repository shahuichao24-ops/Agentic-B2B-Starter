# Agentic B2B Starter

> **An Apple HIG full-stack boilerplate tailored for Product Managers & Agentic AI coding (Cursor, Claude Code, Antigravity).**  
> *Transform business specs into production-grade, interactive prototypes in minutes using deterministic engineering guardrails.*

[English](README.md) | [简体中文](README.zh-CN.md)

[![React 19](https://img.shields.io/badge/React-19.x-blue?logo=react)](https://react.dev/)
[![Tailwind CSS v4](https://img.shields.io/badge/Tailwind-v4.x-38bdf8?logo=tailwindcss)](https://tailwindcss.com/)
[![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-Radix-black)](https://ui.shadcn.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-Pydantic%20v2-orange)](https://sqlmodel.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 💡 The Core Philosophy

When building with **Agentic Coding (Cursor, Claude Code, Antigravity)**, Product Managers and indie hackers face two recurring nightmares:
1. **Visual Degradation**: Left unguided, AI models hallucinate random hex colors, clutter screens with question-mark tooltips, invent verbose secondary instructions, and generate clumsy icon blocks.
2. **Backend Architecture Drift**: AI models naturally default to naive CRUD without soft deletes, leak data across tenants, omit pagination, and crash unexpectedly upon database constraints.

**Agentic B2B Starter** enforces a simple, battle-tested doctrine:
> **Use deterministic engineering rules to suppress AI hallucinations.**  
> *"Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining."*

By pairing an Apple HIG visual system with a hardened FastAPI backend governed by **`AGENTS.md`**, this boilerplate turns AI into an obedient, professional engineering partner.

---

## 🏛️ Architecture Overview

```text
Agentic-B2B-Starter/
├── AGENTS.md                # 🤖 AI coding specification (.cursorrules)
├── AGENTS.zh-CN.md          # 🤖 AI coding specification (Chinese version)
├── create-saas-project.sh   # 🚀 10-second instant project generator
├── docs/                    # 📚 Design system & Lucide business icon library
│   └── icon-library.md
├── frontend/                # 🎨 Apple HIG frontend (React 19 + Tailwind v4 + shadcn)
└── backend/                 # ⚙️ Contract-first B2B backend (FastAPI + SQLModel)
```

---

## 💎 Engineering Highlights

### 1. Frontend: Strict Apple Human Interface Guidelines (HIG)
- **Visual Canvas**: `bg-background` (System Gray 6) with pure white Inset Grouped cards (`rounded-xl border shadow-sm`).
- **No Manual Style Leaks**: AI is strictly forbidden from writing arbitrary hex colors; all elements inherit directly from semantic design tokens.
- **De-Manualization**: Eliminates repetitive subtitles and `<DialogDescription>` noise. Layouts and breadcrumbs are self-explanatory.
- **Text-Only Row Actions**: Replaces isolated, ambiguous icon buttons with clear, semantic text buttons (*"Edit"*, *"Delete"*).
- **Viewport Protection**: Data tables include horizontal scroll bounds; modals have strict `max-h-[88vh]` overflow fallbacks.
- **Centered Data Alignment**: All attribute columns, status badges, switches, and actions are centered by default.

### 2. Backend: Contract-First & Defense-in-Depth
- **Strict 3-Layer Architecture**: Clean isolation across `models/` (entities & DTOs), `services/` (business logic), and `api/v1/` (routers & response envelopes).
- **Unified Response Envelopes**: All endpoints return structured `ApiResponse(code, message, data)`.
- **Physical Multi-Tenant Isolation**: Database session queries automatically inject `tenant_id` filters via low-level interceptors, physically preventing cross-tenant data leaks.
- **Soft-Delete by Default**: Prevents accidental physical data wiping (`is_deleted = True` with audit timestamps).
- **Graceful Constraint Handling**: Intercepts `IntegrityError` and `RequestValidationError` cleanly into HTTP 400/422 envelopes without leaking internal tracebacks.

---

## 🚀 Quick Start

### Option A: Generate a New Project in 10 Seconds (Recommended)

```bash
# Clone the template skeleton into your desired workspace
./create-saas-project.sh ~/projects/my-new-saas
```

### Option B: Run Locally from Source

#### 1. Backend API (Port 8000)

```bash
cd backend

# Create and activate virtual environment (uv recommended)
uv venv
source .venv/bin/activate

# Install dependencies and start server
uv pip install -e .
python run.py
```
- 📖 Interactive Swagger API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- 💡 Reset database and seed clean demo data: `python run.py --reset-db`

#### 2. Frontend Dashboard (Port 5173)

```bash
cd frontend

# Install dependencies
pnpm install

# Start Vite dev server
pnpm dev
```
- 🖥️ Dashboard Preview: [http://localhost:5173](http://localhost:5173)

---

## 🎯 PM Direct Prompts (How to Direct AI)

When collaborating in Cursor, Claude Code, or Antigravity, inject `AGENTS.md` into the agent's context and issue concise, business-level instructions:

- **Full-Stack Feature**:
  > *"Add a [Supplier Qualification Review] module, including paginated table, review status state machine (pending/approved/revision/rejected), and dialog for revision notes. Enable soft-delete."*
  - *The AI will automatically build the Model, Service, and API router, and generate the corresponding Apple HIG Inset Card table and modal without visual regressions.*
- **Frontend-Only View**:
  > *"Add a [Compliance Dashboard] page fetching statistics from backend endpoints and rendering 4 soft status indicator cards."*
- **Backend-Only Service**:
  > *"Add a batch Excel import endpoint for suppliers with credit code regex validation."*

---

## 📜 License & Acknowledgments

- Released under the [MIT License](LICENSE).
- **Acknowledgments & Upstream Attribution**:
  - The frontend dashboard foundation is adapted from [satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin) (MIT License), extensively re-engineered with Apple HIG Inset Grouped visual hierarchy, compact toolbar streams, and Agentic design governance.
  - The backend is powered by FastAPI and SQLModel.

---

## ⚠️ Disclaimer

This repository serves as a personal engineering baseline and design standard for **Product Manager & Agentic Coding workflows**. It is optimized for rapid prototyping, architecture validation, and self-contained project derivation.

**This project does not offer dedicated customer support or high-frequency issue triage.** You are warmly welcomed to Fork, Star, and adapt it to your own commercial and prototype projects!
