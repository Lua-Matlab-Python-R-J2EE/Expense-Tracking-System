from backend import db_helper

# Can add many more test for each function within db_helper.py

def test_retrieve_expenses_by_date_aug_15():
    expenses = db_helper.retrieve_expenses_by_date(expense_date="2024-08-15")
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"

def test_retrieve_expenses_by_date_invalid_date():
    expenses = db_helper.retrieve_expenses_by_date(expense_date="2099-08-15")
    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    expenses = db_helper.fetch_expense_summary("2099-01-01","2099-12-31")
    assert len(expenses) == 0
