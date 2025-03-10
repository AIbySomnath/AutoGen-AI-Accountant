import sqlite3
import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date():
    return f"{random.randint(2020, 2025)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

def seed_database():
    # Connect to SQLite database
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        account_number TEXT,
        account_type TEXT,
        balance REAL,
        created_date TEXT,
        status TEXT,
        owner_id INTEGER,
        branch_id INTEGER,
        interest_rate REAL,
        credit_limit REAL,
        currency TEXT,
        overdraft_limit REAL,
        last_transaction_date TEXT,
        account_manager TEXT,
        notes TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        account_id INTEGER,
        transaction_date TEXT,
        amount REAL,
        transaction_type TEXT,
        description TEXT,
        category TEXT,
        merchant TEXT,
        status TEXT,
        reference_number TEXT,
        payment_method TEXT,
        currency TEXT,
        exchange_rate REAL,
        location TEXT,
        notes TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        zip_code TEXT,
        country TEXT,
        date_of_birth TEXT,
        gender TEXT,
        account_manager TEXT,
        created_date TEXT,
        notes TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS account_summary (
        id INTEGER PRIMARY KEY,
        account_id INTEGER,
        month TEXT,
        total_deposits REAL,
        total_withdrawals REAL,
        average_balance REAL,
        interest_earned REAL,
        fees_charged REAL,
        total_transactions INTEGER,
        highest_balance REAL,
        lowest_balance REAL,
        ending_balance REAL,
        status TEXT,
        account_manager TEXT,
        notes TEXT
    )
    ''')

    # Insert sample data
    for _ in range(50):
        cursor.execute('''
        INSERT INTO accounts (account_number, account_type, balance, created_date, status, owner_id, branch_id, interest_rate, credit_limit, currency, overdraft_limit, last_transaction_date, account_manager, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (random_string(10), random.choice(['savings', 'checking']), round(random.uniform(1000, 10000), 2), random_date(), random.choice(['active', 'inactive']), random.randint(1, 50), random.randint(1, 10), round(random.uniform(0.5, 5.0), 2), round(random.uniform(500, 5000), 2), random.choice(['USD', 'EUR', 'GBP']), round(random.uniform(100, 1000), 2), random_date(), random_string(10), random_string(20)))

        cursor.execute('''
        INSERT INTO transactions (account_id, transaction_date, amount, transaction_type, description, category, merchant, status, reference_number, payment_method, currency, exchange_rate, location, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (random.randint(1, 50), random_date(), round(random.uniform(10, 500), 2), random.choice(['deposit', 'withdrawal']), random_string(20), random.choice(['food', 'entertainment', 'utilities']), random_string(10), random.choice(['completed', 'pending']), random_string(10), random.choice(['credit_card', 'debit_card', 'cash']), random.choice(['USD', 'EUR', 'GBP']), round(random.uniform(0.8, 1.2), 2), random_string(10), random_string(20)))

        cursor.execute('''
        INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, country, date_of_birth, gender, account_manager, created_date, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (random_string(8), random_string(10), random_string(5) + '@example.com', random_string(10), random_string(20), random_string(10), random_string(10), random_string(5), random_string(10), random_date(), random.choice(['male', 'female']), random_string(10), random_date(), random_string(20)))

        cursor.execute('''
        INSERT INTO account_summary (account_id, month, total_deposits, total_withdrawals, average_balance, interest_earned, fees_charged, total_transactions, highest_balance, lowest_balance, ending_balance, status, account_manager, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (random.randint(1, 50), 'current_month', round(random.uniform(1000, 5000), 2), round(random.uniform(500, 2000), 2), round(random.uniform(1000, 10000), 2), round(random.uniform(10, 100), 2), round(random.uniform(5, 50), 2), random.randint(10, 50), round(random.uniform(1000, 10000), 2), round(random.uniform(200, 5000), 2), round(random.uniform(1000, 10000), 2), random.choice(['active', 'inactive']), random_string(10), random_string(20)))

    # Commit and close
    conn.commit()
    conn.close()
