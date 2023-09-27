import streamlit as st
from transformers import pipeline

# Load the chatbot model
model = pipeline("text-generation", model="cardiff-nlp/twitter-roberta-base-chatbot")

# Define the banking dataset
banking_data = ["What is the interest rate for a savings account?", "How do I deposit money into my account?", "What is the routing number for my bank?"]

# Define the chatbot UI
ui = st.sidebar.select_option("Select a conversation topic", banking_data)

# Start the chatbot
st.sidebar.chatbot(model, ui)

# Train the chatbot
st.sidebar.train_chatbot(model, banking_data)

# Run the chatbot
st.sidebar.run_chatbot(model, ui)
