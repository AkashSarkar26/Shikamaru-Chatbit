import streamlit as st
import google.generativeai as genai
from PIL import Image
import base64

# Configure Gemini API Key
genai.configure(api_key="AIzaSyACz1W3zd5ZpEi_wkcRlQWWi532VBolamk")

# Set up Streamlit page configuration
st.set_page_config(page_title="Shikamaru Chatbot", layout="wide")

# Load Shikamaru background image and logo
bg_image = r"C:\Users\User\Downloads\Shikamaru\background.jpg"
logo_image = r"C:\Users\User\Downloads\Shikamaru\kunai.png"

# Function to convert image to base64 for embedding in CSS
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Apply background styling
def set_background(image_path):
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

        .stApp {{
            background-image: url("data:image/jpeg;base64,{get_image_as_base64(image_path)}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            padding: 10px 10px 10px 10px;
        }}

        .header {{
            text-align: center;
            padding: 20px;
            font-family: 'Press Start 2P', cursive;
            color: black;
        }}

        .logo {{
            width: 100px; 
            height: 100px;
            vertical-align: middle;
        }}

        .response {{
            background-color: black;
            padding: 10px;
            border-radius: 8px;
            color: white; 
        }}

        .thinking-text {{
            color: black;
            font-weight: bold; 
            font-size: 30px; 
        }}

        .input-label {{
            color: black; 
            font-family: 'Press Start 2P', cursive;
        }}

        .stTextInput input {{
            font-family: 'Press Start 2P', cursive; 
        
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_background(bg_image)

# Title and Header Section
st.markdown(
    f"""
    <div class="header">
        <img src="data:image/png;base64,{get_image_as_base64(logo_image)}" class="logo" />
        <h1 style="display: inline; color:black; font-family: 'Press Start 2P', cursive;">Shikamaru Chatbot</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chatbox Section
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

# Input field for user query
st.markdown('<p class="input-label">Your question for Shikamaru:</p>', unsafe_allow_html=True)
user_input = st.text_input("", key="user_input")  # No label for the input field

# Process user query
if user_input:
    st.write("<p class='thinking-text'>Thinking... 🤔</p>",
             unsafe_allow_html=True)
    try:
        # Use the GenerativeModel to generate content
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)

        # Display the response text
        st.markdown(f'<div class="response"><b>Shikamaru:</b> {response.text}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# End chat box section
st.markdown('</div>', unsafe_allow_html=True)
