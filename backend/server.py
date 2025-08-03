from http.client import HTTPException

from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

# In terminal, go to folder that contains the server.py, then run 'fastapi dev ./server.py'

# from logging_setup import setup_logger
# logger = setup_logger('server')

app = FastAPI()

class Expense(BaseModel):
    amount      : float
    category    : str
    notes       : str

class DateRange(BaseModel):
    start_date : date
    end_date   : date


# /http_endpoint/expense_date
# GET method to retrieve record for a simple query (POST for more complex queries)
# @app.get("/expenses/{expenses_date}")
@app.get("/expenses/{expenses_date}", response_model=List[Expense])
def get_expenses(expenses_date: date):
    expenses = db_helper.retrieve_expenses_by_date(expenses_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the DB")

    return expenses

# 2nd endpoint is POST
# whatever data is on UI is what is inserted in DB, and previous entries are deleted.
@app.post("/expenses/{expenses_date}", response_model=List[Expense])
def add_or_update_expenses(expenses_date: date, expenses:List[Expense]):
    # first deleting all expenses previous expenses for the input data
    db_helper.delete_expenses_by_date(expenses_date)

    # we have a list of expense retrieved for the given date, so extract 1-by-1
    for expense in expenses:
        db_helper.create_expense(expenses_date, expense.amount, expense.category, expense.notes)

    return [ { "amount"  : expense.amount,
               "category": expense.category,
               "notes"   : expense.notes
             } for expense in expenses ]


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the DB.")

    # Get the total of all categories within the date range
    total = sum( [ row['sum(amount)'] for row in data ] )
    # print("total: " , total)

    braakdown = {}

    # Get the category total as sent total of all categories within the date range
    for row in data:
        percentage = 100*row['sum(amount)']/total if total !=0 else 0
        braakdown[row['category']] = {
                "total"     : row['sum(amount)'],
                "percentage": percentage
        }

    # Create such a structure of total and percentages to be passed to the front end
    # {
    #     "rent":     {"total": 1234, "percentage":34.45},
    #     "shopping": {"total": 2234, "percentage":64.45}
    # }

    return braakdown
