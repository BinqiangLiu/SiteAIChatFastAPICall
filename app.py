import streamlit as st
import requests
import json

def query_fastapi(question):
    url = "https://binqiangliu-siteaichatfastapi.hf.space/query/"
    headers = {"Content-Type": "application/json"}
    data = {"query": question}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error from API: {response.status_code}")

# 示例查询
question = st.text_input("Enter your question:")
if st.button('Get AI Response'):
    try:
        result = query_fastapi(question)
        st.write("AI Response:", result.get("AI Response"))
        st.write("Sources:", result.get("Sources"))
        print("AI Response:", result.get("AI Response"))
        print("Sources:", result.get("Sources"))
    except Exception as e:
        print(e)
