# Expense Tracking System — Full-Stack Data Application

## Overview

A full-stack personal finance application for tracking, categorising, and analysing expenses in real time. Built with a three-tier architecture: Streamlit frontend, FastAPI REST backend, and MySQL database — demonstrating end-to-end software engineering beyond a typical data science notebook.

**Key capabilities:**
- Add, update, and delete expense records via an interactive UI
- Analytics by category (monthly view in progress)
- REST API (FastAPI) with request validation (Pydantic)
- Unit tests for the database layer (pytest); API endpoints checked manually with Postman
- Persistent storage with a structured relational database schema

---

## Architecture
```
┌─────────────────────┐
│   Streamlit UI      │  ← Interactive frontend (Add/Update, Analytics)
└─────────┬───────────┘
          │ HTTP
          ▼
┌─────────────────────┐
│   FastAPI Server    │  ← REST API (CRUD endpoints, analytics routes)
└─────────┬───────────┘
          │ SQL
          ▼
┌─────────────────────┐
│   MySQL Database    │  ← Persistent storage (expenses, categories)
└─────────────────────┘
```

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | Streamlit | Interactive web UI |
| Backend | FastAPI | High-performance REST API |
| Database | MySQL | Relational data persistence |
| Testing | pytest + Postman | DB-layer unit tests; manual API checks |

---

## Project Structure
```
expense-tracking-system/
├── frontend/         → Streamlit UI pages and components
├── backend/          → FastAPI server and API endpoints
├── tests/            → Unit tests for the database layer
├── db_schema/        → schema.sql (creates the DB + sample rows) and table description
└── requirements.txt  → Python dependencies
```

---

## Setup & Running Locally

### 1. Clone and install dependencies
```bash
git clone https://github.com/Lua-Matlab-Python-R-J2EE/expense-tracking-system.git
cd expense-tracking-system
pip install -r requirements.txt
```

### 2. Create the database and set your credentials

Option A, Docker (no MySQL install): creates a random password in `.env`, starts MySQL 8 and loads the sample data.
```bash
bash scripts/start_db.sh       # stop later with: docker stop expense-mysql
```

Option B, your own MySQL server:
```bash
mysql -u root -p < db_schema/schema.sql
cp .env.example .env      # then put your MySQL password in .env (never committed)
```

### 3. Start the FastAPI backend
```bash
cd backend
fastapi dev server.py
# API available at http://localhost:8000
```

### 4. Launch the Streamlit frontend
```bash
cd frontend
streamlit run app.py
# App available at http://localhost:8501
```

---

## Features & Status

| Feature | Backend | Frontend | Tests |
|---|---|---|---|
| Add / Update Expenses | ✅ | ✅ | DB layer (pytest) |
| Analytics by Category | ✅ | ✅ | DB layer (pytest) |
| Analytics by Month | 🔄 In progress | 🔄 In progress | ⏳ Pending |
| Logging (file log, API + DB layers) | ✅ | — | — |

---

## Running the tests
```bash
mysql -u root -p < db_schema/schema.sql   # tests expect the sample rows
pytest
```

---

## Development Approach

Features are built vertically — backend -> frontend -> tests — completing one feature end-to-end before starting the next. This ensures each slice of functionality is fully working and tested before moving on, and keeps the codebase in a continuously deployable state.

---

