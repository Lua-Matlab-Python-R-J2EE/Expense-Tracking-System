'''
- Website:  https://streamlit.io/
- From terminal, run 'streamlit run ./app.py' to see the output of streamlite UI file
'''

import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def add_update_tab():
    # Default date is Hard-coded date - no need to change
    selected_date = st.date_input("Enter Date", datetime(year=2024,month=8,day=1), label_visibility="collapsed")

    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json() # result from DB query
        # st.write(existing_expenses)
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    catagories = ['Food','Shopping','Rent', 'Entertainment', 'Other']
    expenses   = []

    # create a form with for loop to populate these retrieved data in 'existing_expenses'
    with st.form(key="expense_form"):
        # add column headers
        col1, col2, col3 = st.columns(3)
        with col1:
            # st.subheader("Amount")
            st.text("Amount")
        with col2:
            # st.subheader("Category")
            st.text("Category")
        with col3:
            # st.subheader("Notes")
            st.text("Notes")

        # table with fixed number of 5 rows and 3 columns to add the data from the DB
        for i in range(5):

            # the 'existing_expenses' could have more or less than 5 entries, so we need to check it's length first
            if i < len(existing_expenses):
                amount   = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes    = existing_expenses[i]['notes']
            else:
                amount   = 0.0
                category = "Shopping"
                notes    = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input   = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=catagories, index=catagories.index(category), key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input    = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'amount'   : amount_input,
                'category' : category_input,
                'notes'    : notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button: # the expenses in DB get updated
            # filter expense variable for 0.0 values in amount
            filtered_expenses = [expense for expense in expenses if expense['amount']>0.0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200: # can include check for many more http status codes
                st.success("Expenses updated successfully")
            else:
                st.error("Failed to update expenses")




