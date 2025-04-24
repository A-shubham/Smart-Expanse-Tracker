import sqlite3

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()
    
    conn = sqlite3.connect('expense_tracker.db')
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("✅ Database initialized and seeded successfully.")

if __name__ == '__main__':
    init_db()
