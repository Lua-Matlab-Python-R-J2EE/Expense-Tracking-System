'''
- Website: https://streamlit.io/
- To run this Streamlit UI, navigate to the frontend folder in your terminal, then execute:
  
      streamlit run ./app.py

  This will launch a local Streamlit web interface in your default browser.
'''

# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
import streamlit as st             # Streamlit for building interactive web apps
from datetime import datetime      # Used to work with and format date inputs
import requests                    # Used for making HTTP requests to the backend API
import pandas as pd                # Used for data manipulation and visualization in table/chart form


# -------------------------------------------------------------------------
# Backend API base URL (FastAPI server)
# -------------------------------------------------------------------------
API_URL = "http://localhost:8000"


# -------------------------------------------------------------------------
# Function: analytics_tab
# -------------------------------------------------------------------------
def analytics_tab():
    """
    Streamlit UI function for expense analytics and visualization.

    Workflow:
    1. Allows the user to select a start and end date.
    2. Sends these dates to the FastAPI backend (`/analytics/` endpoint) via POST request.
    3. Receives category-wise total and percentage breakdown of expenses.
    4. Displays the data visually using a bar chart and a formatted summary table.

    API Endpoint Used:
        - POST /analytics/
          Payload: {"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"}
          Response: {
              "Rent": {"total": 1200, "percentage": 30.0},
              "Food": {"total": 2800, "percentage": 70.0}
          }
    """

    # ---------------------------------------------------------------------
    # Step 1: Create two side-by-side date input fields (start and end)
    # ---------------------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        # Default start date (can be adjusted)
        start_date = st.date_input("Start date", datetime(2024, 8, 1))
    with col2:
        # Default end date
        end_date = st.date_input("End date", datetime(2024, 8, 5))

    # ---------------------------------------------------------------------
    # Step 2: On button click, send request to backend to fetch analytics
    # ---------------------------------------------------------------------
    if st.button("Get Analytics"):
        # The payload must match backend's expected date format (ISO 8601)
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        # POST request to the FastAPI analytics endpoint
        response = requests.post(f"{API_URL}/analytics/", json=payload)

        # -----------------------------------------------------------------
        # Step 3: Handle backend response (success or failure)
        # -----------------------------------------------------------------
        if response.status_code == 200:
            # Convert response JSON (dict) into a Python object
            response = response.json()
            # st.write(response)  # Optional: uncomment to debug API response
        else:
            # Show error message if request fails
            st.error("Failed to retrieve results for these dates")
            return  # Exit early if request fails

        # -----------------------------------------------------------------
        # Step 4: Transform backend response into a DataFrame for visualization
        # -----------------------------------------------------------------
        # Example structure after transformation:
        # {
        #   "category":   ["Rent", "Shopping"],
        #   "total":      [123, 345],
        #   "percentage": [4, 6]
        # }
        data = {
            "category": list(response.keys()),
            "total": [response[category]['total'] for category in response],
            "percentage": [response[category]['percentage'] for category in response]
        }

        # Create DataFrame for analysis and visualization
        df = pd.DataFrame(data)

        # Sort categories by percentage of spending (descending order)
        df_sorted = df.sort_values(by="percentage", ascending=False)

        # -----------------------------------------------------------------
        # Step 5: Display analytics results in chart and table format
        # -----------------------------------------------------------------
        st.title("Expense Breakdown by Category")

        # Bar chart: categories on x-axis, percentage of total spending on y-axis
        # Index set to 'category' for meaningful x-axis labels
        st.bar_chart(data=df_sorted.set_index("category")['percentage'])

        # Format numeric columns for display (2 decimal places)
        df_sorted["total"] = df_sorted['total'].map("{:.2f}".format)
        df_sorted["percentage"] = df_sorted['percentage'].map("{:.2f}".format)

        # Display the final formatted summary table below the chart
        st.table(df_sorted)
