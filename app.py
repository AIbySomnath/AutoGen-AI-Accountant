import streamlit as st
from agent1 import Agent1
from generate_db import seed_database
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if the database is already seeded
if not os.path.exists("db_seeded.flag"):
    logging.info("Seeding the database with initial data...")
    seed_database()
    with open("db_seeded.flag", "w") as f:
        f.write("true")

st.title("AI-Powered Account Summary")

agent1 = Agent1()

query = st.text_input("Enter your request (e.g., 'Give me the account summary for the current month'):")

if st.button("Submit") and query:
    try:
        raw_data, summary, sql_query = agent1.process_request(query)
        st.subheader("SQL Query:")
        st.code(sql_query)
        st.subheader("Raw Data:")
        st.write(raw_data)
        st.subheader("Summary:")
        st.write(summary)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        logging.error(f"Error processing request: {e}")
