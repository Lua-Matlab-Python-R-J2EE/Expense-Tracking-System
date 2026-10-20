# Database Structure

The app uses one MySQL table, `expenses`, in the database `expense_manager`.
`schema.sql` in this folder creates it and loads sample rows.

## `expenses`

| Column         | Type                     | Description                               |
|----------------|--------------------------|-------------------------------------------|
| `id`           | INT, PK, AUTO_INCREMENT  | Unique identifier for each expense        |
| `expense_date` | DATE, NOT NULL           | Date of the expense                       |
| `amount`       | FLOAT, NOT NULL          | Amount spent                              |
| `category`     | VARCHAR(255), NOT NULL   | Rent, Food, Shopping, Entertainment, Other |
| `notes`        | TEXT                     | Optional free-text note                   |

## How the code uses it

| Function (backend/db_helper.py) | SQL                                                          |
|---------------------------------|--------------------------------------------------------------|
| `create_expense`                | INSERT one row (parameterised query)                         |
| `retrieve_expenses_by_date`     | SELECT all rows for one date                                 |
| `delete_expenses_by_date`       | DELETE all rows for one date                                 |
| `fetch_expense_summary`         | SUM(amount) GROUP BY category between two dates              |

The API saves a day by deleting that date's rows and inserting the new list.
