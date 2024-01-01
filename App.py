from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai 

# Load environment variables
load_dotenv()

# Configure generative AI with the API key
os.environ['GOOGLE_API_KEY']='AIzaSyCCda9IZfuXVSDyrYhRbJs7FkPNgFXZqvE'
genai.configure(api_key="AIzaSyCCda9IZfuXVSDyrYhRbJs7FkPNgFXZqvE")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit configuration
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# User input
input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask the question")

# After submission
if submit_button:
    response_text = get_gemini_response(input_text)
    st.write(response_text)
