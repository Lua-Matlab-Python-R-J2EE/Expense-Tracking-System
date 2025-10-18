"""
=========================================================================================
TEST MODULE: db_helper.py
-----------------------------------------------------------------------------------------
PURPOSE:
    This file contains unit tests for verifying the functionality of the database helper
    module (`db_helper.py`) used in the Expense Management System project.

USAGE:
    Run all tests using the following command in terminal:

        pytest ./test_db_helper.py

    or simply:

        pytest

NOTES:
    - These tests depend on a pre-populated MySQL database (configured in db_helper.py).
    - Each test verifies expected behavior of specific CRUD operations.
    - Assertions confirm correctness of query results returned by the database helper.

AUTHOR:
    (Your Name)
=========================================================================================
"""

from backend import db_helper   # Importing database helper module to be tested


# --------------------------------------------------------------------------------------
# TEST CASE 1: Retrieve expenses for a known date (expected to return exactly one record)
# --------------------------------------------------------------------------------------
def test_retrieve_expenses_by_date_aug_15():
    """
    Verifies that retrieving expenses for a valid date returns the correct record.

    Expected behavior:
        - Query for '2024-08-15' should return exactly one expense entry.
        - The returned record should have:
            amount   = 10
            category = "Shopping"
            notes    = "Bought potatoes"
    """
    expenses = db_helper.retrieve_expenses_by_date(expense_date="2024-08-15")

    # Check the query returned exactly one row
    assert len(expenses) == 1

    # Validate all expected field values in the returned row
    assert expenses[0]['amount']   == 10
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes']    == "Bought potatoes"


# --------------------------------------------------------------------------------------
# TEST CASE 2: Retrieve expenses for a future/invalid date (expected to return no records)
# --------------------------------------------------------------------------------------
def test_retrieve_expenses_by_date_invalid_date():
    """
    Verifies that querying for a date with no matching entries returns an empty result set.

    Expected behavior:
        - Querying for '2099-08-15' (a future date) should return an empty list.
    """
    expenses = db_helper.retrieve_expenses_by_date(expense_date="2099-08-15")

    # No records should exist for this future date
    assert len(expenses) == 0


# --------------------------------------------------------------------------------------
# TEST CASE 3: Fetch expense summary for an invalid date range (expected to return none)
# --------------------------------------------------------------------------------------
def test_fetch_expense_summary_invalid_range():
    """
    Verifies that fetching an expense summary for a date range with no data returns an empty list.

    Expected behavior:
        - Query for range '2099-01-01' to '2099-12-31' should yield zero rows.
    """
    expenses = db_helper.fetch_expense_summary("2099-01-01", "2099-12-31")

    # The database should return no grouped summary entries for this empty range
    assert len(expenses) == 0
