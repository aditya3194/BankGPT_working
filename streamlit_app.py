import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import cohere


# App title
st.set_page_config(page_title="India MoF-WIP")

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input):
    response = co.chat(
	prompt_input, 
	model="command", 
	temperature=0.3
    )
    return response.text

# # User-provided prompt
# if prompt := st.chat_input():
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)
	    
openai_api_key = st.text_input('Cohere API Key')
co = cohere.Client(openai_api_key)
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

