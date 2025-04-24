from flask import Flask, render_template, request, redirect, url_for
from model import get_all_categories, add_expense, get_expenses_by_user
from model import get_monthly_summary, get_category_summary
from datetime import datetime

app = Flask(__name__)

# Create a custom filter for date formatting
@app.template_filter('format_date')
def format_date(value):
    if isinstance(value, str):  # If the value is a string, try to convert it to a date
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime('%Y-%m-%d') if value else ''

# Hardcoding user_id for now (you can later implement login)
USER_ID = 1

@app.route('/report')
def report():
    monthly = get_monthly_summary(USER_ID)
    category = get_category_summary(USER_ID)
    return render_template('report.html', monthly=monthly, category=category)

@app.route('/')
def index():
    categories = get_all_categories()
    expenses = get_expenses_by_user(USER_ID)
    return render_template('index.html', categories=categories, expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    category_id = request.form['category']
    amount = float(request.form['amount'])
    expense_date = request.form['date']
    description = request.form['description']
    
    add_expense(USER_ID, category_id, amount, expense_date, description)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
