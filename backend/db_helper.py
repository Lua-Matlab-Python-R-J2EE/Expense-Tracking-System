# Import necessary modules
import mysql.connector                 # MySQL database connector for Python
from contextlib import contextmanager  # Used to create context managers (for 'with' statements)
from pprint import pprint              # Pretty-printing for more readable console output
from logging_setup import setup_logger # Custom logging setup module

# Initialize a logger specific to this module for consistent logging
logger = setup_logger('db_helper')


@contextmanager
def get_db_cursor(commit=False):
    """
    Context manager that provides a MySQL cursor object.
    Automatically handles opening and closing the connection.
    Optionally commits transactions if 'commit=True'.
    
    Args:
        commit (bool): If True, commits the transaction when exiting the context.
    
    Yields:
        cursor (mysql.connector.cursor.MySQLCursorDict): A dictionary-based cursor object.
    """
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host     = "localhost",
        user     = "sql_tutorial",
        password = "mysql_Pa55word!-.",
        database = "expense_manager"
    )
    # Create a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)

    # Provide the cursor to the calling code
    yield cursor

    # Commit the transaction if specified
    if commit:
        connection.commit()

    # Close cursor and connection to release resources
    cursor.close()
    connection.close()


# ------------------------- CRUD OPERATION: CREATE -------------------------
def create_expense(expense_date, amount, category, notes):
    """
    Inserts a new expense record into the 'expenses' table.
    
    Args:
        expense_date (str): The date of the expense (format: 'YYYY-MM-DD').
        amount (str or float): The monetary amount of the expense.
        category (str): Category of the expense (e.g., 'Food', 'Travel').
        notes (str): Optional descriptive notes about the expense.
    """
    logger.info(f"create_expense function called with params {expense_date}, {amount}, {category}, {notes}")
    
    # Use context manager to handle DB connection and auto-commit
    with get_db_cursor(commit=True) as cursor:
        # Execute parameterized INSERT query to avoid SQL injection
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


# ------------------------- CRUD OPERATION: READ -------------------------
def retrieve_expenses_by_date(expense_date):
    """
    Retrieves all expense records for a specific date.
    
    Args:
        expense_date (str): Date to fetch expenses for (format: 'YYYY-MM-DD').
    
    Returns:
        list[dict]: A list of expense records as dictionaries.
    """
    logger.info(f"retrieve_expenses_by_date function called with date {expense_date}")
    
    with get_db_cursor() as cursor:
        # Execute SELECT query using parameter substitution
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        # Return all matching records as a list of dictionaries
        return cursor.fetchall()


# ------------------------- CRUD OPERATION: DELETE -------------------------
def delete_expenses_by_date(expense_date):
    """
    Deletes all expense records for a specific date.
    
    Args:
        expense_date (str): Date of expenses to delete (format: 'YYYY-MM-DD').
    """
    logger.info(f"delete_expenses_by_date function called with date {expense_date}")
    
    with get_db_cursor(commit=True) as cursor:
        # Execute DELETE query for the specified date
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )


# ---------------------- AGGREGATE QUERY: SUMMARY ----------------------
def fetch_expense_summary(start_date, end_date):
    """
    Retrieves the sum of expenses grouped by category within a date range.
    
    Args:
        start_date (str): Start date of the range (format: 'YYYY-MM-DD').
        end_date (str): End date of the range (format: 'YYYY-MM-DD').
    
    Returns:
        list[dict]: Each record contains a category and its total sum of expenses.
    """
    logger.info(f"fetch_expense_summary function called between dates {start_date} - {end_date}")
    
    with get_db_cursor() as cursor:
        # Execute a grouped SELECT query to get total expenses per category
        cursor.execute(
            "SELECT category, sum(amount) FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category;",
            (start_date, end_date)
        )
        # Return aggregated results as a list of dictionaries
        return cursor.fetchall()


# ---------------------- MAIN BLOCK: MODULE TESTING ----------------------
if __name__ == "__main__":
    """
    This block is executed only when the script is run directly.
    It performs basic sanity checks for the functions defined above.
    """
    print("--------------------------------------------------------------")

    # Example: create a sample expense record (commented out by default)
    # create_expense(expense_date="2025-08-01", amount="50", category="Food", notes="Dosa and idli")

    # Retrieve expenses for a given date
    pprint(retrieve_expenses_by_date("2025-08-02"))
    print("--------------------------------------------------------------")

    # Example: delete expenses by date (commented out by default)
    # delete_expenses_by_date("2025-08-01")
    print("--------------------------------------------------------------")

    # Verify deletion by attempting to retrieve again
    pprint(retrieve_expenses_by_date("2025-08-02"))
    print("--------------------------------------------------------------")

    # Fetch expense summary for a date range
    pprint(fetch_expense_summary(start_date="2024-08-02", end_date="2024-08-05"))
    print("--------------------------------------------------------------")
