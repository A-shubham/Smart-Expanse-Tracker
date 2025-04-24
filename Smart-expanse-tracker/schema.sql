-- Drop tables if they exist
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS expenses;

-- Users Table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories Table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE
);

-- Expenses Table
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    category_id INTEGER,
    amount REAL NOT NULL,
    expense_date DATE,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Indexes
CREATE INDEX idx_user ON expenses(user_id);
CREATE INDEX idx_category ON expenses(category_id);
CREATE INDEX idx_expense_date ON expenses(expense_date);

-- Seed data
INSERT INTO categories (category_name) VALUES ('Food'), ('Travel'), ('Bills'), ('Shopping');
INSERT INTO users (username, email) VALUES ('aman', 'a.shubham2499@gmail.com');
