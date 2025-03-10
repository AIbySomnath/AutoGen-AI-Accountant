import streamlit as st
from agent1 import Agent1

st.title("AI-Powered Account Summary")

agent1 = Agent1()

query = st.text_input("Enter your request (e.g., 'Give me the account summary for the current month'):")

if st.button("Submit") and query:
    raw_data, summary = agent1.process_request(query)
    
    st.subheader("Raw Data:")
    st.write(raw_data)
    
    st.subheader("Summary:")
    st.write(summary)