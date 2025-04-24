import sqlite3

DB_NAME = 'expense_tracker.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Enable dict-like access
    return conn

def get_all_categories():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return categories

def add_expense(user_id, category_id, amount, expense_date, description):
    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO expenses (user_id, category_id, amount, expense_date, description)
           VALUES (?, ?, ?, ?, ?)''',
        (user_id, category_id, amount, expense_date, description)
    )
    conn.commit()
    conn.close()

def get_expenses_by_user(user_id):
    conn = get_db_connection()
    expenses = conn.execute(
        '''SELECT e.expense_id, c.category_name, e.amount, e.expense_date, e.description
           FROM expenses e
           JOIN categories c ON e.category_id = c.category_id
           WHERE e.user_id = ?
           ORDER BY e.expense_date DESC''',
        (user_id,)
    ).fetchall()
    conn.close()
    return expenses

def get_monthly_summary(user_id):
    conn = get_db_connection()
    summary = conn.execute("""
        SELECT strftime('%Y-%m', expense_date) AS month,
               SUM(amount) AS total_amount
        FROM expenses
        WHERE user_id = ?
        GROUP BY month
        ORDER BY month DESC
    """, (user_id,)).fetchall()
    conn.close()
    return summary

def get_category_summary(user_id):
    conn = get_db_connection()
    summary = conn.execute("""
        SELECT c.category_name, SUM(e.amount) AS total_amount
        FROM expenses e
        JOIN categories c ON e.category_id = c.category_id
        WHERE e.user_id = ?
        GROUP BY c.category_name
        ORDER BY total_amount DESC
    """, (user_id,)).fetchall()
    conn.close()
    return summary
