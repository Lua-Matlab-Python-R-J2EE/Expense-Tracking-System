import mysql.connector
from contextlib import contextmanager
from pprint import pprint
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host     = "localhost",
        user     = "sql_tutorial",
        password = "mysql_Pa55word!-.",
        database = "expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

# CRUD's C (create or insert or update)
def create_expense(expense_date, amount, category, notes):
    logger.info(f"create_expense function called with params {expense_date}, {amount}, {category}, {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

# CRUD's R (retrieve or fetch)
def retrieve_expenses_by_date(expense_date):
    logger.info(f"retrieve_expenses_by_date function called with date {expense_date}")
    with get_db_cursor() as cursor:
        # print(f"Date parameter type, value: {type(expense_date)}, {expense_date}")
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        return cursor.fetchall()

# CRUD's D (delete)
def delete_expenses_by_date(expense_date):
    logger.info(f"delete_expenses_by_date function called with date {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )

# get sum of expenses by category between the two dates
def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary function called between dates {start_date} - {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT category, sum(amount) FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category;",
            (start_date, end_date)
        )
        return cursor.fetchall()

if __name__=="__main__":
    # basic check for functions within 'db_helper.py' module

    # create a dummy expense by date
    # create_expense(expense_date="2025-08-01", amount="50", category="Food", notes="Dosa and idli")
    print("--------------------------------------------------------------")

    # retrieve it by date
    pprint( retrieve_expenses_by_date("2025-08-02") )
    print("--------------------------------------------------------------")

    # delete it by date
    # delete_expenses_by_date("2025-08-01")
    print("--------------------------------------------------------------")

    # retrieve it by date to check it has been deleted
    pprint( retrieve_expenses_by_date("2025-08-02") )
    print("--------------------------------------------------------------")

    # retrieve data between start_date and end_date
    pprint( fetch_expense_summary(start_date="2024-08-02", end_date="2024-08-05") )
    print("--------------------------------------------------------------")
