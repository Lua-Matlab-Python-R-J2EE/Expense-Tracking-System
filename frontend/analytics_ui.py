'''
- Website:  https://streamlit.io/
- From terminal, go to the frontend folder, run 'streamlit run ./app.py' to see the output of streamlite UI file
'''

import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start date", datetime(2024, 8, 1))
    with col2:
        end_date   = st.date_input("Start date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        # the payload dates need to be in datetime format (what is going into the DB to fetch the query)
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date"   : end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        if response.status_code == 200:
            response = response.json()  # result from DB query
            # st.write( response ) # convert 'response' to table using pandas dataframe and then display on screen
        else:
            st.error("Failed to retrieve results for these dates")

        # # Create 'response' to a structure of this type the following
        # df = pd.DataFrame({
        #     "category"   :  ["Rent", "Shopping"],
        #     "total"      :  [123, 345],
        #     "Percentage" :  [4, 6]
        # })

        data = {
            "category"   :  list(response.keys()),
            "total"      :  [response[category]['total'] for category in response],
            "percentage" :  [response[category]['percentage'] for category in response]
        }
        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="percentage", ascending=False)

        st.title("Expense Breakdown by Category")
        # st.bar_chart(data=df_sorted) # the index in the data frame should be categories not integers
        st.bar_chart(data=df_sorted.set_index("category")['percentage'])

        df_sorted["total"]      = df_sorted['total'].map("{:.2f}".format)
        df_sorted["percentage"] = df_sorted['percentage'].map("{:.2f}".format)

        st.table(df_sorted)
