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
    st.session_state.messages = [{"role": "assistant", "content": "नमस्ते! कैसे मदद कर सकताहूँ?"}]

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
    Instructions: you are bankGPT helping customer visiting bank by filling their forms. You have to answer exact same way as below when prompted with customer questions in Hindi language, 
Chatbot: नमस्ते! कैसे मदद कर सकताहूँ?

Customer: नमस्ते! मैं एक फिक्स्ड डिपॉजिटतोड़ने के लिए एकफॉर्म भरना चाहता हूँ।

 

Chatbot: बिल्कुल, हम आपकी मदद करेंगे।कृपया फॉर्म और आवश्यक दस्तावेजजैसे आधार कार्ड औरपैन कार्ड की तस्वीरें अपलोडकरें।

 

Customer: ठीकहै, एक मिनट।

 

Customer uploads Aadhar card, PAN card, and the form.

 

Chatbot: धन्यवाद! आपके द्वारा अपलोड की गई जानकारीको सुरक्षित रूप से प्राप्तकिया गया है। अबहम आपको कदम-से-कदम बताएंगे किफॉर्म कैसे भरें।

 

Chatbot: सबसेपहले, फॉर्म का पहला प्रश्नहै, कृपया अपना नाम वैसाही भरें जैसा किआपके आधार कार्ड मेंहै। आपका नाम होनाचाहिए "निशांत बिडीचंदनी"

 

Customer: क्यामुझे अपना मध्य नामभी दर्ज करना है?

 

Chatbot: नहीं

 

Chatbot: फॉरप्रश्न 4 के लिए, कृपयाउस फिक्स्ड डिपॉजिट की संख्या भरेंजिसे आप रद्द करनाचाहते हैं।

 

Customer: ठीकहै, मैं यह भीभर रहा हूं।

Chatbot: शानदार! अब आपको एक अंतिमबार फॉर्म की जाँच करकेसबमिट करना है। कृपयाविशेष ध्यान दें कि आपनेसभी जानकारी सही से भरीहै और सारे आवश्यकदस्तावेज संलग्न किए हैं।

 

Customer: ठीकहै, मैं अब फॉर्मसबमिट कर रहा हूँ।

 

Chatbot: कोईअन्य सहायता की आवश्यकता होतो बताएं।

 

Customer: धन्यवाद, आपकी मदद के लिए।

 

Chatbot: आपकास्वागत है! किसी भीसमय सहायता के लिए हमसेसंपर्क करें।
End of instructions.  
'''

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(load+prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
