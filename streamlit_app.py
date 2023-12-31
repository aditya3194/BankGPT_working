import streamlit as st
import cohere
import random
import time
import openai

# App title
st.set_page_config(page_title="India MoF-WIP")
with st.sidebar:
      st.markdown(
        f"""
        <style>
            .top-left-image {{
                display: flex;
                flex-direction: column;
                align-items: center;
                top: 0;
            }}
        </style>
        <div class="top-left-image">
            <img src="https://github.com/aditya3194/BankGPT_working/raw/73b65bed439cb01d6ad477258b1376f5224ee95c/MicrosoftTeams-image%20(1).png" width="200" alt="Image" />
        </div>
        """,
        unsafe_allow_html=True,
    )



# with st.sidebar:
#       st.markdown(
#         f"""
#         <style>
#             .bottom-left-image {{
#                 position: absolute;
#                 bottom: 0;
#                 left: 0;
#                 padding: 10px;
#             }}
#         </style>
#         <div class="bottom-left-image">
#             <img src="https://github.com/aditya3194/BankGPT_working/raw/ec792ff8b7c28f232f3eb80c915e09d3012cad53/mic.png" width="50" alt="Image" />
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
      
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Replace with your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Define a dictionary of user inputs and corresponding responses (rule-based)
responses = {
'नमस्ते! मैं एक फिक्स्ड डिपॉजिट तोड़ने के लिए एक फॉर्म भरना चाहता हूँ। ' : 'बिल्कुल, हम आपकी मदद करेंगे। कृपया फॉर्म और आवश्यक दस्तावेज जैसे आधार कार्ड और पैन कार्ड की तस्वीरें अपलोड करें।' ,
'ठीक है, अपलोड कर चुके है|' : '''धन्यवाद! आपके द्वारा अपलोड की गई जानकारी को सुरक्षित रूप से प्राप्त किया गया है।\n
कृपया यह सुनिश्चित करें कि आपका विवरण सही है।\n

नाम: अनुराग शर्मा \n
जन्म तिथि: 03 मार्च 1994 \n
पता: बिल्डिंग 52, मैत्री पार्क सोसायटी, कोलाबा, मुंबई - 400022 \n
PAN कार्ड नंबर: BKSUB1234 \n
आधार नंबर: 1234 3211 2345''',
'हाँ, सही हैं।' : 'अब हम आपको कदम-से-कदम बताएंगे कि फॉर्म कैसे भरें। सबसे पहले, फॉर्म का पहला प्रश्न है, कृपया अपना नाम वैसा ही भरें जैसा कि आपके आधार कार्ड में है। आपका नाम होना चाहिए "अनुराग शर्मा"| ' ,
'क्या मुझे अपना मध्य नाम भी दर्ज करना है? ' : 'नहीं | क्या आपका खाता स्थानीय है, या NRE/NRO है?।' ,
'मेरे पास केवल स्थानीय बचत खाता है।' : 'ठीक है, कृपया उसे टिक करें। इसके बाद, प्रश्न 4 के लिए, कृपया उस फिक्स्ड डिपॉजिट की संख्या भरें जिसे आप रद्द करना चाहते हैं।' ,
'ठीक है, फिक्स्ड डिपॉजिट की संख्या हैं -213882| मैं यह भर रहा हूं। ' : 'अब प्रश्न 5 के लिए, कृपया वह राशि दर्ज करें जो फिक्स्ड डिपॉजिट में है।' ,
'राशि हैं रु. 20,000| मैंने इसे भर लिया है।' : 'शानदार! अब आपको एक अंतिम बार फॉर्म की जाँच करके सबमिट करना है। कृपया विशेष ध्यान दें कि आपने सभी जानकारी सही से भरी है और सारे आवश्यक दस्तावेज संलग्न किए हैं।' ,
'फ़ॉर्म में सब कुछ ठीक है।' : 'बहुत अच्छा! अब कृपया उपर दी गई तस्वीर के अनुसार फ़ॉर्म पर हस्ताक्षर करें।' ,
'हो गया' : '"स्थान" के लिए, कृपया मुंबई लिखें और "तारीख" के लिए, कृपया आज की तारीख डालें, जो कि 1 अक्टूबर 2023 है। कृपया इसके बाद फ़ॉर्म सबमिट करें। मैं एक डिजिटल कॉपी भी सबमिट कर रहा हूँ।' ,
'ठीक है, मैं अब फॉर्म सबमिट कर रहा हूँ। ' : 'कोई अन्य सहायता की आवश्यकता होतो बताएं।' ,
'धन्यवाद, आपकी मदद के लिए। ' : 'आपका स्वागत है! किसी भी समय सहायता के लिए हम से संपर्क करें।' ,




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
    st.session_state.messages = [{"role": "assistant", "content": "नमस्ते!में कैसे मदद कर सकता हूँ?"}]

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
      time.sleep(5)
      return uploaded_file

def image_show():
      st.image("https://github.com/aditya3194/BankGPT_working/raw/master/Bank%20Tick.png", caption="Form Preview", use_column_width=True)
      

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

                        if prompt in ("फ़ॉर्म में सब कुछ ठीक है।"):
                              file = image_show()
                            #   time.sleep(5)
                            
                else:
                        response = generate_response_co(load+prompt)
                        # response = generate_response_oi(load+prompt)
    st.write(response)
    if response in ("बिल्कुल, हम आपकी मदद करेंगे। कृपया फॉर्म और आवश्यक दस्तावेज जैसे आधार कार्ड और पैन कार्ड की तस्वीरें अपलोड करें।"):
        file = file_uploader()
    message = {"role": "assistant", "content":response}
    st.session_state.messages.append(message)
