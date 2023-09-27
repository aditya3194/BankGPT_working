import streamlit as st
import openai

# Set your OpenAI API key here
api_key = "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"
openai.api_key = api_key

# Define a function to interact with the ChatGPT model
def chat_with_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful banking chatbot."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message["content"]

# Create a Streamlit app
st.title("Banking Chatbot")

# Define a text input for user messages
user_input = st.text_input("You:", "")

# Handle user input and display responses
if st.button("Send"):
    if user_input:
        st.text("ChatGPT:")
        chat_response = chat_with_gpt3(user_input)
        st.text(chat_response)
