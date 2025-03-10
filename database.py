from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, text
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd
from config import DB_CONFIG
import logging

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_number = Column(String)
    account_type = Column(String)
    balance = Column(Float)
    created_date = Column(Date)
    status = Column(String)
    owner_id = Column(Integer)
    branch_id = Column(Integer)
    interest_rate = Column(Float)
    credit_limit = Column(Float)
    currency = Column(String)
    overdraft_limit = Column(Float)
    last_transaction_date = Column(Date)
    account_manager = Column(String)
    notes = Column(String)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_date = Column(Date)
    amount = Column(Float)
    transaction_type = Column(String)
    description = Column(String)
    category = Column(String)
    merchant = Column(String)
    status = Column(String)
    reference_number = Column(String)
    payment_method = Column(String)
    currency = Column(String)
    exchange_rate = Column(Float)
    location = Column(String)
    notes = Column(String)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    account_manager = Column(String)
    created_date = Column(Date)
    notes = Column(String)

class AccountSummary(Base):
    __tablename__ = 'account_summary'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    month = Column(String)
    total_deposits = Column(Float)
    total_withdrawals = Column(Float)
    average_balance = Column(Float)
    interest_earned = Column(Float)
    fees_charged = Column(Float)
    total_transactions = Column(Integer)
    highest_balance = Column(Float)
    lowest_balance = Column(Float)
    ending_balance = Column(Float)
    status = Column(String)
    account_manager = Column(String)
    notes = Column(String)

engine = create_engine(DB_CONFIG['database_url'])
Session = sessionmaker(bind=engine)

def execute_query(query):
    session = Session()
    try:
        logging.info(f"Executing query: {query}")
        result = session.execute(text(query))
        data = result.fetchall()
        df = pd.DataFrame(data, columns=result.keys())
        return df
    finally:
        session.close()

# Create tables
Base.metadata.create_all(engine)
