#Working...

import streamlit as st
import requests
import json

import timeit
import datetime

import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Website AI Chat Assistant - Open Source Version", layout="wide")
st.subheader("Welcome to Open Website AI Chat Assistant Life Enhancing with AI!")
st.write("Important notice: This Open Website AI Chat Assistant is offered for information and study purpose only and by no means for any other use. Any user should never interact with the AI Assistant in any way that is against any related promulgated regulations. The user is the only entity responsible for interactions taken between the user and the AI Chat Assistant.")
css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)  

current_datetime_0= datetime.datetime.now()
print(f"Anything happens, this ST app will execute from top down. @ {current_datetime_0}")
print()

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def query_fastapi(question):
    url = "https://binqiangliu-siteaichatfastapi.hf.space/query/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"
        #保险起见，建议始终采用f''的形式以及配合使用{}
    }
#    headers = {"Content-Type": "application/json"}
    data = {"query": question}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error from API: {response.status_code}")

# 示例查询
question = st.text_input("Enter your question:")
if st.button('Get AI Response'):
    with st.spinner('Fetching AI response...'):   
        try:
            ai_response = query_fastapi(question)
            ai_response_content=ai_response['AIResponse']
            ai_response_source=ai_response['Sources']
            #st.write("AI Response:", result.get("AI Response"))
            
            st.write("AI Response:", ai_response_content)
            #st.write("Sources:", ai_response_source)
            # 使用st.write打印Sources的内容
            st.write("Sources:")
            for source in ai_response_source:
                st.write(source)
            
            print("AI Response:", ai_response_content)
            #print("Sources:", ai_response_source)
            print("Sources:")
            for source in ai_response_source:
                print(source)
                #ai_response_source中有一个键值source？
            #Sources: ['https://www.hbsr.com/...cine', '...', 'https://www.hbsr.com/contact']
            
        except Exception as e:
            print(e)
