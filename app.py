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
        ai_response = query_fastapi(question)
        ai_response_content=ai_response['AIResponse']
        ai_response_source=ai_response['Sources']
        #st.write("AI Response:", result.get("AI Response"))
        
        st.write("AI Response:", ai_response_content)
        st.write("Sources:", ai_response_source)

        print("AI Response:", ai_response_content)
        print("Sources:", ai_response_source)
    except Exception as e:
        print(e)


        #st.write("AI Response:", result.get("AI Response"))
        #st.write("Sources:", result.get("Sources"))
        #print("AI Response:", result.get("AI Response"))
        #print("Sources:", result.get("Sources"))
        # result.get("AI Response"))???
        # result.get("Sources"))???       
