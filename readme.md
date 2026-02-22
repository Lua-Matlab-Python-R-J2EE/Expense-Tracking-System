# Expense Tracking System — Full-Stack Data Application

## Overview

A full-stack personal finance application for tracking, categorising, and analysing expenses in real time. Built with a three-tier architecture: Streamlit frontend, FastAPI REST backend, and MySQL database — demonstrating end-to-end software engineering beyond a typical data science notebook.

**Key capabilities:**
- Add, update, and delete expense records via an interactive UI
- Real-time analytics by category and monthly trends
- RESTful API with full unit and integration test coverage
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
| Testing | Postman + Unit Tests | API validation and DB coverage |

---

## Project Structure
```
expense-tracking-system/
├── frontend/         → Streamlit UI pages and components
├── backend/          → FastAPI server and API endpoints
├── tests/            → Unit tests and integration tests
├── db_schema/        → Database schema and ER diagram
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

### 2. Start the FastAPI backend
```bash
cd backend
fastapi dev server.py
# API available at http://localhost:8000
```

### 3. Launch the Streamlit frontend
```bash
cd frontend
streamlit run app.py
# App available at http://localhost:8501
```

---

## Features & Status

| Feature | Backend | Frontend | Tests |
|---|---|---|---|
| Add / Update Expenses | ✅ | ✅ | ✅ |
| Analytics by Category | ✅ | ✅ | ✅ |
| Analytics by Month | 🔄 In progress | 🔄 In progress | ⏳ Pending |
| Logging & Monitoring | ✅ | — | — |

---

## Development Approach

Features are built vertically — backend -> frontend -> tests — completing one feature end-to-end before starting the next. This ensures each slice of functionality is fully working and tested before moving on, and keeps the codebase in a continuously deployable state.

---

