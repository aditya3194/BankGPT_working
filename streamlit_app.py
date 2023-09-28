import streamlit as st
import cohere
import random
import time
import openai

# App title
st.set_page_config(page_title="India MoF-WIP")

# Define a dictionary of user inputs and corresponding responses (rule-based)
responses = {
    "balance": "Your account balance is $5,000.",
    "transaction history": "You have three recent transactions: \n1. $100 deposit on 2023-09-25 \n2. $50 withdrawal on 2023-09-24 \n3. $200 deposit on 2023-09-23",
    "interest rates": "The current interest rate for savings accounts is 2.5% per annum.",
    "contact info": "You can reach our customer support at support@bank.com or call us at +1-800-123-4567.",
    "help": "I'm here to provide information about your account and our services. How can I assist you today?",
    "नमस्ते! मैं एक फिक्स्ड डिपॉजिटतोड़ने के लिए एकफॉर्म भरना चाहता हूँ।" : "बिल्कुल, हम आपकी मदद करेंगे।कृपया फॉर्म और आवश्यक दस्तावेजजैसे आधार कार्ड औरपैन कार्ड की तस्वीरें अपलोडकरें।" ,
	"ठीक है, एक मिनट।" : "धन्यवाद! आपके द्वारा अपलोड की गई जानकारीको सुरक्षित रूप से प्राप्तकिया गया है। अबहम आपको कदम-से-कदम बताएंगे किफॉर्म कैसे भरें। सबसेपहले, फॉर्म का पहला प्रश्नहै, कृपया अपना नाम वैसाही भरें जैसा किआपके आधार कार्ड मेंहै। आपका नाम होनाचाहिए 'अनुराग शर्मा'" ,
	"क्या मुझे अपना मध्य नामभी दर्ज करना है?" : "नहीं | प्रश्न 4 के लिए, कृपयाउस फिक्स्ड डिपॉजिट की संख्या भरें जिसे आप रद्द करना चाहते हैं।" ,
	"ठीक है, मैं यह भी भर रहा हूं।" : "शानदार! अब आपको एक अंतिमबार फॉर्म की जाँच करके सबमिट करना है। कृपया विशेष ध्यान दें कि आपने सभी जानकारी सही से भरी है और सारे आवश्यक दस्तावेज संलग्न किए हैं।" ,
	"ठीक है, मैं अब फॉर्मसबमिट कर रहा हूँ।" : "कोईअन्य सहायता की आवश्यकता होतो बताएं।" ,
	"धन्यवाद, आपकी मदद के लिए।" : "आपका स्वागत है! किसी भी समय सहायता के लिए हमसेसंपर्क करें।"

}

# with st.sidebar:
#        st.title('India MoF')

#        st.text('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') # OPenAI key
#        openai.api_key = st.text_input('Add your Open AI API Key')
       
#     #    st.text('c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ') # Cohere Key
#     #    cohere_api_key = st.text_input('Add your Cohere API Key')
# 	#    cohere_api_key = 'c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ'

#        st.button('Proceed!')
#        st.warning('Please enter your credentials and click proceed!', icon='⚠️')
#     #    if not (cohere_api_key):
#     #           st.warning('Please enter your credentials!', icon='⚠️')
#     #    else:
#     #           st.success('Proceed to entering your prompt message!', icon='👉')

cohere_api_key = 'c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ'
co = cohere.Client(cohere_api_key)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "नमस्ते! कैसे मदद कर सकताहूँ?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
chat_history = []

# openai.api_key = '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'
# OpenAI function
def generate_response_oi(prompt_input):
        response = openai.ChatCompletion.create(
  			model="gpt-3.5-turbo",
			messages=[
					{"role": "system", "content": "You are a helpful assistant."},
					{"role": "user", "content": prompt_input},
				]
				)
        user_message = {"user_name": "User", "text": prompt_input}
        bot_message = {"user_name": "Chatbot", "text": response['choices'][0]['message']['content']}
        chat_history.append(user_message)
        chat_history.append(bot_message)
        return response['choices'][0]['message']['content']

# Cohere function
def generate_response_co(prompt_input):
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

def file_uploader():
      uploaded_file = st.file_uploader('Upload relevant documents',accept_multiple_files=True)
      return uploaded_file

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

load ='''
    Instructions: Consider that you are helpful chatbot for Indian bank employee, helping customer in every possible way by respondnig them back with human like conversation.
'''

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
                if prompt in responses:
                        time.sleep(random.randint(1,3))
                        response = responses[prompt]
                        if prompt in ("ठीक है, एक मिनट।"):
                              file = file_uploader()
                              if file is not None:
                                    st.write("Files uploaded successfully!")
                              else:
                                    st.write("Please upload a file to continue.")                    
                else:
                        response = generate_response_co(load+prompt)
                        # response = generate_response_oi(load+prompt)
    st.write(response)
    message = {"role": "assistant", "content":response}
    st.session_state.messages.append(message)
