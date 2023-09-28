import streamlit as st
# from hugchat import hugchat
# from hugchat.login import Login
import cohere


# App title
st.set_page_config(page_title="India MoF-WIP")

with st.sidebar:
	st.title('India MoF')
	st.text('c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ')
	openai_api_key = st.text_input('Cohere API Key')
	st.button('Proceed!')
	if not (openai_api_key):
	    st.warning('Please enter your credentials!', icon='⚠️')
	else:
	    st.success('Proceed to entering your prompt message!', icon='👉')

co = cohere.Client(openai_api_key)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
chat_history = []

def generate_response(prompt_input):
	response = co.chat(
	prompt_input, 
	model="command-nightly", 
	chat_history= chat_history,
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
	    
# st.text( st.session_state.messages)
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
