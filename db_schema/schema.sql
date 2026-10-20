-- Creates the expense_manager database used by backend/db_helper.py
-- and loads a small set of sample rows (the tests rely on the 2024-08-15 row).
-- Usage: mysql -u root -p < db_schema/schema.sql

CREATE DATABASE IF NOT EXISTS expense_manager;
USE expense_manager;

DROP TABLE IF EXISTS expenses;
CREATE TABLE expenses (
  id           INT          NOT NULL AUTO_INCREMENT,
  expense_date DATE         NOT NULL,
  amount       FLOAT        NOT NULL,
  category     VARCHAR(255) NOT NULL,
  notes        TEXT,
  PRIMARY KEY (id)
);

INSERT INTO expenses (expense_date, amount, category, notes) VALUES
  ('2024-08-01', 1200, 'Rent',          'Monthly rent payment'),
  ('2024-08-01',  300, 'Food',          'Groceries for the week'),
  ('2024-08-02',   50, 'Entertainment', 'Movie tickets'),
  ('2024-08-02',  150, 'Shopping',      'New shoes'),
  ('2024-08-03',  100, 'Food',          'Dinner at a restaurant'),
  ('2024-08-04',   10, 'Other',         'Parking'),
  ('2024-08-05',  350, 'Rent',          'Shared rent payment'),
  ('2024-08-15',   10, 'Shopping',      'Bought potatoes');
