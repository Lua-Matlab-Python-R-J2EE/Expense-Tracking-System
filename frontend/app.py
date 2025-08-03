'''
- Website:  https://streamlit.io/
- From terminal, run 'streamlit run ./app.py' to see the output of streamlite UI file
'''

import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

API_URL = "http://localhost:8000"

st.title("Expense Management System")

tab1, tab2 = st.tabs( ["Add/Update", "Analytics"] )

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()
