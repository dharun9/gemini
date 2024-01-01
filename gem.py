from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image
import SessionState  # You may need to install this package with `pip install streamlit-SessionState`

# Load environment variables
load_dotenv()

# Configure generative AI with the API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyCCda9IZfuXVSDyrYhRbJs7FkPNgFXZqvE'
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Function to load Gemini Pro model and get response
def get_gemini_response(question, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if question != "":
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit configuration
st.set_page_config(page_title="Gemini Q&A Demo")

# Initialize SessionState to persist data across sessions
session_state = SessionState.get(prompt="", questions_and_responses=[])

st.header("Gemini LLM Application")

# User input for prompt
session_state.prompt = st.text_input("Input Prompt:", key="input")

# User input for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to ask about the image
submit_button = st.button("Ask about the image")

# After submission
if submit_button:
    response_text = get_gemini_response(session_state.prompt, image)
    
    # Store the question and response in the list
    session_state.questions_and_responses.append({"question": session_state.prompt, "response": response_text})
    
    st.subheader("The Response is")
    st.write(response_text)

# Display all stored questions and responses
st.subheader("Previous Questions and Responses:")
for item in session_state.questions_and_responses:
    st.write(f"Question: {item['question']}")
    st.write(f"Response: {item['response']}")
    st.write("---")
