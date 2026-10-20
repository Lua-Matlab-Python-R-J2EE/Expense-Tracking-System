'''
- Website: https://streamlit.io/
- To run this Streamlit UI, execute the following command from your terminal:
  
      streamlit run ./app.py

  This will open a local web interface in your browser.
'''

# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
import streamlit as st            # Streamlit: for building the web-based data UI
from datetime import datetime     # For handling date inputs
import requests                   # To communicate with the FastAPI backend via HTTP

# Base URL for the FastAPI server (backend API)
API_URL = "http://localhost:8000"


# -------------------------------------------------------------------------
# Function: add_update_tab
# -------------------------------------------------------------------------
def add_update_tab():
    """
    Streamlit UI function that handles adding or updating expense records.

    Workflow:
    1. Displays a date picker for selecting a specific date.
    2. Fetches existing expenses for that date from the backend (FastAPI).
    3. Displays the expenses in an editable table format (Amount, Category, Notes).
    4. Allows the user to modify or add new entries.
    5. Submits the updated list of expenses back to the backend via a POST request.

    API Endpoints Used:
        - GET  /expenses/{date}     → Fetch existing expenses
        - POST /expenses/{date}     → Update/replace expenses for a given date
    """

    # Default date shown in the UI (hard-coded)
    # You can change this default, but here it’s fixed intentionally for demo/testing
    selected_date = st.date_input(
        "Enter Date",
        datetime(year=2024, month=8, day=1),
        label_visibility="collapsed"
    )

    # ---------------------------------------------------------------------
    # Step 1: Fetch existing expenses for the selected date from FastAPI
    # ---------------------------------------------------------------------
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        # Convert the JSON response to Python objects (list of dicts)
        existing_expenses = response.json()
        # st.write(existing_expenses)  # Debug line (optional)
    else:
        # Display error message on the Streamlit UI if the request fails
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    # ---------------------------------------------------------------------
    # Step 2: Prepare categories and container for new/edited expenses
    # ---------------------------------------------------------------------
    catagories = ['Food', 'Shopping', 'Rent', 'Entertainment', 'Other']
    expenses = []  # List to hold expense dictionaries entered/edited by user

    # ---------------------------------------------------------------------
    # Step 3: Create a Streamlit form for displaying and editing expenses
    # ---------------------------------------------------------------------
    with st.form(key="expense_form"):

        # --- Column headers for table layout ---
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        # -----------------------------------------------------------------
        # Step 4: Render 5 editable rows for expenses (existing or new)
        # -----------------------------------------------------------------
        for i in range(5):
            # If there are existing expenses for this date, pre-fill them
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                # Default blank row for adding new data
                amount = 0.0
                category = "Shopping"
                notes = ""

            # --- Three-column layout for each row (Amount | Category | Notes) ---
            col1, col2, col3 = st.columns(3)

            # Column 1: Amount input (float, cannot be negative)
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{i}",
                    label_visibility="collapsed"
                )

            # Column 2: Category dropdown (select from predefined list)
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=catagories,
                    index=catagories.index(category),
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )

            # Column 3: Notes text input field
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}",
                    label_visibility="collapsed"
                )

            # Append row data to the expenses list
            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        # -----------------------------------------------------------------
        # Step 5: Form submission logic
        # -----------------------------------------------------------------
        submit_button = st.form_submit_button()

        if submit_button:
            # Filter out expenses with zero amount before sending to backend
            filtered_expenses = [
                expense for expense in expenses if expense['amount'] > 0.0
            ]

            # Send filtered expense data as JSON to the FastAPI POST endpoint
            response = requests.post(
                f"{API_URL}/expenses/{selected_date}",
                json=filtered_expenses
            )

            # Display result based on response status
            if response.status_code == 200:
                st.success("Expenses updated successfully")
            else:
                st.error("Failed to update expenses")
