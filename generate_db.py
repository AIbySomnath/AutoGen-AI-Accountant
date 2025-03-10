import sqlite3

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

    # Static realistic data
    accounts_data = [
        ('1234567890', 'savings', 5000.00, '2022-01-01', 'active', 1, 1, 1.2, 1000.00, 'USD', 500.00, '2023-12-01', 'Manager_1', 'Note_1'),
        ('2345678901', 'checking', 3000.00, '2022-02-01', 'active', 2, 2, 1.0, 1500.00, 'EUR', 700.00, '2023-12-02', 'Manager_2', 'Note_2'),
        ('3456789012', 'savings', 7000.00, '2022-03-01', 'inactive', 3, 3, 1.5, 2000.00, 'GBP', 800.00, '2023-12-03', 'Manager_3', 'Note_3'),
        # Add more static data as needed
    ]

    transactions_data = [
        (1, '2023-12-01', 100.00, 'deposit', 'Salary', 'income', 'Employer', 'completed', 'REF123', 'direct_deposit', 'USD', 1.0, 'New York', 'Salary for December'),
        (2, '2023-12-02', 50.00, 'withdrawal', 'Groceries', 'expense', 'Supermarket', 'completed', 'REF124', 'credit_card', 'USD', 1.0, 'New York', 'Grocery shopping'),
        (3, '2023-12-03', 200.00, 'deposit', 'Freelance work', 'income', 'Client', 'completed', 'REF125', 'paypal', 'EUR', 1.0, 'Berlin', 'Freelance project payment'),
        # Add more static data as needed
    ]

    customers_data = [
        ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm St', 'Springfield', 'IL', '62701', 'USA', '1980-01-01', 'male', 'Manager_1', '2022-01-01', 'VIP customer'),
        ('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak St', 'Springfield', 'IL', '62702', 'USA', '1990-02-02', 'female', 'Manager_2', '2022-02-01', 'Frequent traveler'),
        ('Alice', 'Johnson', 'alice.johnson@example.com', '1122334455', '789 Pine St', 'Springfield', 'IL', '62703', 'USA', '1985-03-03', 'female', 'Manager_3', '2022-03-01', 'High net worth individual'),
        # Add more static data as needed
    ]

    account_summary_data = [
        (1, 'current_month', 1500.00, 500.00, 6000.00, 60.00, 10.00, 20, 7000.00, 5000.00, 6500.00, 'active', 'Manager_1', 'Summary for December'),
        (2, 'current_month', 2000.00, 1000.00, 4000.00, 40.00, 20.00, 30, 5000.00, 3000.00, 4000.00, 'active', 'Manager_2', 'Summary for December'),
        (3, 'current_month', 1000.00, 300.00, 8000.00, 80.00, 15.00, 25, 9000.00, 7000.00, 7000.00, 'inactive', 'Manager_3', 'Summary for December'),
        # Add more static data as needed
    ]

    # Insert sample data
    for account in accounts_data:
        cursor.execute('''
        INSERT INTO accounts (account_number, account_type, balance, created_date, status, owner_id, branch_id, interest_rate, credit_limit, currency, overdraft_limit, last_transaction_date, account_manager, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', account)

    for transaction in transactions_data:
        cursor.execute('''
        INSERT INTO transactions (account_id, transaction_date, amount, transaction_type, description, category, merchant, status, reference_number, payment_method, currency, exchange_rate, location, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', transaction)

    for customer in customers_data:
        cursor.execute('''
        INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, country, date_of_birth, gender, account_manager, created_date, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', customer)

    for summary in account_summary_data:
        cursor.execute('''
        INSERT INTO account_summary (account_id, month, total_deposits, total_withdrawals, average_balance, interest_earned, fees_charged, total_transactions, highest_balance, lowest_balance, ending_balance, status, account_manager, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', summary)

    # Commit and close
    conn.commit()
    conn.close()
