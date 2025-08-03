# 💰 Expense Tracking System

## 📋 Project Description

A comprehensive expense management application built with FastAPI backend and Streamlit frontend, featuring real-time analytics and MySQL database integration for efficient personal finance tracking.

---

## 🏗️ Project Structure

```
expense-tracking-system/
├── 📂 frontend/         → Streamlit UI components and pages
├── 📂 backend/          → FastAPI server and API endpoints
├── 📂 tests/            → Unit tests and integration tests
├── 📄 requirements.txt  → Python dependencies
└── 📄 README.md         → Project documentation
```

---

## 🚀 Project Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/expense-tracking-system.git
cd expense-tracking-system
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Run the FastAPI Server**
```bash
cd backend
fastapi dev server.py
```
*Server will be available at: `http://localhost:8000`*

### 4. **Run the Streamlit App**
```bash
cd frontend
streamlit run app.py
```
*App will be available at: `http://localhost:8501`*

---

## 🏛️ Architecture Diagram

```
┌─────────────────────┐
│   Streamlit UI      │  ← User Interface (Add/Update, Analytics)
│   (Frontend)        │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   FastAPI Server    │  ← REST API Endpoints
│   (Backend)         │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   MySQL Database    │  ← Data Storage (Expenses, Categories)
│   (Data Layer)      │
└─────────────────────┘
```

**Key Components:**
- **Frontend Layer**: Interactive Streamlit interface
- **API Layer**: RESTful FastAPI endpoints
- **Data Layer**: MySQL database with CRUD operations
- **Analytics**: Real-time expense categorization and reporting

---

# 📋 EXPENSE TRACKING SYSTEM - Development Roadmap

## ✅ Phase 1: Database Foundation
| Component | Description | Status |
|-----------|-------------|---------|
| 🗄️ **MySQL Database Setup** | Reference: `15.3_and_15.4_IMP.py` | ✅ **Complete** |
| 🔧 **CRUD Operations** | `db_helper.py` implementation | ✅ **Complete** |  
| 🧪 **Database Unit Tests** | Test coverage for `db_helper.py` | ✅ **Complete** |

---

## ✅ Phase 2: FastAPI Backend Development
| Endpoint | Description | Status |
|----------|-------------|---------|
| 📝 **Add/Update Expenses** | Fetch expenses by date for population | ✅ **Complete** |
| 🧪 **Postman Testing** | API endpoint validation | ✅ **Complete** |
| 📊 **Analytics by Category** | Category-wise expense breakdown | ✅ **Complete** |
| 🧪 **Postman Testing** | Category analytics validation | ✅ **Complete** |
| 📅 **Analytics by Month** | Monthly expense trends | 🚧 **In Progress** |
| 🧪 **Postman Testing** | Monthly analytics validation | ⏳ **Pending** |

---

## ✅ Phase 3: System Monitoring
| Component | Description | Status |
|-----------|-------------|---------|
| 📝 **Logging System** | `server.py` and `db_helper.py` logging | ✅ **Complete** |

---

## 🚧 Phase 4: Streamlit Frontend
| Screen | Description | Status |
|--------|-------------|---------|
| ➕ **Add/Update Screen** | Expense entry and modification interface | ✅ **Complete** |
| 📊 **Analytics by Category** | Visual category-wise reports | ✅ **Complete** |
| 📅 **Analytics by Month** | Monthly trend visualization | 🚧 **In Progress** |

---

## 🔄 Development Methodology

> **Vertical Development Approach**: We follow a complete feature-to-feature development cycle:

1. 🎯 **Add/Update Screen** → Frontend + Backend + Testing
2. 📊 **Analytics by Category** → Frontend + Backend + Testing  
3. 📅 **Analytics by Month** → Frontend + Backend + Testing

This ensures each feature is fully functional before moving to the next, enabling continuous testing and user feedback.

---

## 🎨 Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | 🎨 Streamlit | Interactive web interface |
| **Backend** | ⚡ FastAPI | High-performance API server |
| **Database** | 🗄️ MySQL | Reliable data persistence |
| **Testing** | 🧪 Postman | API endpoint validation |

---
