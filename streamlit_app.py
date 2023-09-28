import streamlit as st
import cohere
import random
import time

# App title
st.set_page_config(page_title="India MoF-WIP")

# Define a dictionary of customer inputs and corresponding responses (rule-based)
responses = {
    "balance": "Your account balance is $5,000.",
    "transaction history": "You have three recent transactions: \n1. $100 deposit on 2023-09-25 \n2. $50 withdrawal on 2023-09-24 \n3. $200 deposit on 2023-09-23",
    "interest rates": "The current interest rate for savings accounts is 2.5% per annum.",
    "contact info": "You can reach our customer support at support@bank.com or call us at +1-800-123-4567.",
    "help": "I'm here to provide information about your account and our services. How can I assist you today?",
}

with st.sidebar:
		st.title('India MoF')
		# st.text('c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ')
		# openai_api_key = st.text_input('Cohere API Key')
		openai_api_key = 'c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ'
		st.button('Proceed!')
		if not (openai_api_key):
			st.warning('Please enter your credentials!', icon='⚠️')
		else:
			st.success('Proceed to entering your prompt message!', icon='👉')

co = cohere.Client(openai_api_key)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "chatbot", "content": "नमस्ते! कैसे मदद कर सकताहूँ?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
chat_history = []


def generate_response(prompt_input):
		response = co.chat(
		prompt_input, 
		model="command-nightly", 
		# chat_history= chat_history,
		temperature=0.3
		)
		customer_message = {"customer_name": "customer", "text": prompt_input}
		bot_message = {"customer_name": "Chatbot", "text": response.text}


		chat_history.append(customer_message)
		chat_history.append(bot_message)
		
		return response.text

# customer-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "customer", "content": prompt})
    with st.chat_message("customer"):
        st.write(prompt)

load ='''
    Instructions: Consider that you are bankGPT helping customer visiting bank by filling their forms. Reply bank in Hindi language if possible
'''

if st.session_state.messages[-1]["role"] != "chatbot":
    with st.chat_message("chatbot"):
        with st.spinner("Thinking..."):
                if prompt in responses:
                        time.sleep(random.randint(1,3))
                        response = responses[prompt]
                else:
                        response = generate_response(load+prompt)
    st.write(response)
    message = {"role": "chatbot", "content":response}
    st.session_state.messages.append(message)
