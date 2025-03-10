import streamlit as st
from agent1 import Agent1
from generate_db import seed_database

# Check if the database is already seeded
try:
    with open("db_seeded.flag", "r") as f:
        db_seeded = f.read().strip() == "true"
except FileNotFoundError:
    db_seeded = False

if not db_seeded:
    seed_database()
    with open("db_seeded.flag", "w") as f:
        f.write("true")

st.title("AI-Powered Account Summary")

agent1 = Agent1()

query = st.text_input("Enter your request (e.g., 'Give me the account summary for the current month'):")

if st.button("Submit") and query:
    raw_data, summary = agent1.process_request(query)
    
    st.subheader("Raw Data:")
    st.write(raw_data)
    
    st.subheader("Summary:")
    st.write(summary)
