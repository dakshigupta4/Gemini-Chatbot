from dotenv import load_dotenv
load_dotenv()    ##loading environment variables
import streamlit as st
import os
import google.generativeai as genai
# load api_key
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model=genai.GenerativeModel("gemini-pro")
def gen_ai_response(question):
    response = model.generate_content(question)
    return response.text 
st.set_page_config(page_title="Q & A")
st.title('llm')
input=st.text_input("enter your question")
submit=st.button("submit")
if submit:
    result=gen_ai_response(input)
    st.write(result)
