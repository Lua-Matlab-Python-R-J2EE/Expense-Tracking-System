'''
- Website:  https://streamlit.io/
- To run this Streamlit UI, open your terminal and execute:

      streamlit run ./app.py

  This will launch a local Streamlit web interface in your default browser.
  Make sure both backend (FastAPI server) and frontend (this Streamlit app)
  are running simultaneously for full functionality.
'''

# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
import streamlit as st                   # Streamlit for interactive frontend
from add_update_ui import add_update_tab # Custom module for Add/Update Expense UI
from analytics_ui import analytics_tab   # Custom module for Analytics/Reports UI


# -------------------------------------------------------------------------
# Backend API base URL (FastAPI server)
# -------------------------------------------------------------------------
API_URL = "http://localhost:8000"


# -------------------------------------------------------------------------
# Application Title
# -------------------------------------------------------------------------
st.title("Expense Management System")  # Displayed prominently at the top of the web app


# -------------------------------------------------------------------------
# Tab Layout Configuration
# -------------------------------------------------------------------------
# Create two tabs within the Streamlit UI:
#   1. "Add/Update" → for recording or modifying daily expenses
#   2. "Analytics"  → for visualizing expenses and category-wise analysis
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])


# -------------------------------------------------------------------------
# Tab 1: Add or Update Expenses
# -------------------------------------------------------------------------
with tab1:
    """
    The 'Add/Update' tab allows users to:
    - Select a date
    - View, edit, or add expense entries
    - Submit updated records to the FastAPI backend
    """
    add_update_tab()  # Render the Add/Update Expense form from add_update_ui.py


# -------------------------------------------------------------------------
# Tab 2: Expense Analytics
# -------------------------------------------------------------------------
with tab2:
    """
    The 'Analytics' tab allows users to:
    - Select a start and end date
    - Retrieve summary statistics from the backend
    - Visualize data using charts and tables
    """
    analytics_tab()  # Render the Analytics view from analytics_ui.py
