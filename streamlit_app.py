import streamlit as st
# from hugchat import hugchat
# from hugchat.login import Login
import cohere


# App title
st.set_page_config(page_title="India MoF-WIP")


def clear_history():
    st.session_state.history = []
    st.session_state.messages = []
    st.session_state.clear_alert()


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
        
		# st.button('Reset Chat', on_click=reset_conversation)

co = cohere.Client(openai_api_key)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
chat_history = []

def reset_conversation():
  st.session_state.conversation = None
  st.session_state.chat_history = None
  st.session_state.message = None
st.button('Reset Chat', on_click=reset_conversation)

def generate_response(prompt_input):
		response = co.chat(
		prompt_input, 
		model="command-nightly", 
		# chat_history= chat_history,
		temperature=0.3
		)
		user_message = {"user_name": "User", "text": prompt_input}
		bot_message = {"user_name": "Chatbot", "text": response.text}


		chat_history.append(user_message)
		chat_history.append(bot_message)
		
		return response.text

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

load ='''
    Instructions: you are bankGPT helping customer visiting bank by filling their forms. You have to answer exact same way as below when prompted with questions, 
Q1. Who are you? 
A: I am bankGPT, happy to help you
Q2. Do I need to enter my middle name?
A: No, provide me you account number
End of instructions. 
'''

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(load+prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
