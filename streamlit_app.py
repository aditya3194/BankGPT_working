import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Create a Streamlit app
st.title("Banking Chatbot")

# Function to generate responses using ChatGPT
def generate_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            engine="gpt-3.5-turbo",
            prompt=f"User: {user_input}\nChatGPT:",
            max_tokens=50,  # Adjust the response length as needed
            temperature=0.7,  # Adjust the temperature for creativity
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Streamlit UI
with st.form(key='chat_form'):
    user_message = st.text_input("You:", key='user_input')
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    if user_message:
        st.text("ChatGPT:")
        response = generate_response(user_message)
        st.write(response)
    else:
        st.warning("Please enter a message.")

# Instructions
st.info("This is a banking chatbot powered by ChatGPT. Ask questions or seek assistance about banking services.")

