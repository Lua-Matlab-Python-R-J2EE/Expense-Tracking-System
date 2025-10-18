# Import necessary modules and dependencies
from http.client import HTTPException   # Used to raise HTTP-related errors
from fastapi import FastAPI             # The core FastAPI class for creating the web API
from datetime import date               # For handling and validating date objects
import db_helper                        # Local module containing database CRUD operations
from typing import List                 # For type hinting lists (used in Pydantic models and endpoints)
from pydantic import BaseModel           # Base class for defining request/response data models

# -------------------------------------------------------------------------
# Run the API with:
#   fastapi dev ./server.py
# Make sure you are in the directory containing this file when running it.
# -------------------------------------------------------------------------

# (Optional) Example for integrating logging if needed
# from logging_setup import setup_logger
# logger = setup_logger('server')

# Instantiate the FastAPI application
app = FastAPI()


# ----------------------------- Pydantic Models -----------------------------
class Expense(BaseModel):
    """
    Data model representing an individual expense entry.
    
    Attributes:
        amount (float): The monetary value of the expense.
        category (str): The category under which the expense falls (e.g., 'Food', 'Travel').
        notes (str): Optional descriptive notes about the expense.
    """
    amount   : float
    category : str
    notes    : str


class DateRange(BaseModel):
    """
    Data model representing a date range used for analytics queries.
    
    Attributes:
        start_date (date): Start date of the time range (inclusive).
        end_date (date): End date of the time range (inclusive).
    """
    start_date : date
    end_date   : date


# ----------------------------- API ENDPOINTS -----------------------------

# Endpoint: Retrieve all expenses for a specific date
@app.get("/expenses/{expenses_date}", response_model=List[Expense])
def get_expenses(expenses_date: date):
    """
    GET endpoint that retrieves all expenses for a given date.
    
    Args:
        expenses_date (date): The date for which to fetch expenses.
    
    Returns:
        List[Expense]: A list of expense records matching the provided date.
    
    Raises:
        HTTPException: If the database retrieval fails.
    """
    # Retrieve expenses from the database for the specified date
    expenses = db_helper.retrieve_expenses_by_date(expenses_date)

    # If retrieval fails, raise an HTTP exception with status 500
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the DB")

    return expenses


# Endpoint: Insert or update expenses for a given date
@app.post("/expenses/{expenses_date}", response_model=List[Expense])
def add_or_update_expenses(expenses_date: date, expenses: List[Expense]):
    """
    POST endpoint that adds or updates expenses for a specific date.
    - Deletes all existing records for that date.
    - Inserts the new set of expenses received from the client.
    
    Args:
        expenses_date (date): The date associated with the expense records.
        expenses (List[Expense]): A list of Expense objects to be stored.
    
    Returns:
        List[dict]: A confirmation list of the inserted expense records.
    """
    # Delete all previous expense records for the given date
    db_helper.delete_expenses_by_date(expenses_date)

    # Iterate through the list of expenses and insert each one into the database
    for expense in expenses:
        db_helper.create_expense(expenses_date, expense.amount, expense.category, expense.notes)

    # Return the inserted expenses in dictionary format for API response
    return [
        {
            "amount": expense.amount,
            "category": expense.category,
            "notes": expense.notes
        }
        for expense in expenses
    ]


# Endpoint: Generate analytics (summary) for a given date range
@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    """
    POST endpoint that generates an expense summary grouped by category.
    Calculates both total spending and category-wise percentage breakdown
    within the given date range.
    
    Args:
        date_range (DateRange): Object containing 'start_date' and 'end_date'.
    
    Returns:
        dict: A mapping of categories to their total and percentage values.
              Example:
              {
                  "Rent": {"total": 1200, "percentage": 30.0},
                  "Food": {"total": 2800, "percentage": 70.0}
              }
    
    Raises:
        HTTPException: If fetching data from the database fails.
    """
    # Fetch aggregated expense data (category-wise sums) from DB
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    # If data retrieval fails, return a 500 Internal Server Error
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the DB.")

    # Compute total spending across all categories in the date range
    total = sum([row['sum(amount)'] for row in data])

    # Initialize dictionary to store category-wise breakdown
    braakdown = {}

    # For each category, compute total spent and its percentage of the grand total
    for row in data:
        percentage = 100 * row['sum(amount)'] / total if total != 0 else 0
        braakdown[row['category']] = {
            "total": row['sum(amount)'],
            "percentage": percentage
        }

    # Final JSON structure returned to the frontend example:
    # {
    #     "Rent":     {"total": 1234, "percentage": 34.45},
    #     "Shopping": {"total": 2234, "percentage": 64.45}
    # }
    return braakdown
