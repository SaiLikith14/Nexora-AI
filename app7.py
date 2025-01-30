import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Set your Google API key (ensure it is in your .env file)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBW8pLaEmHUnOPYsTBmiOM1GfEkLvzHsZA"  # Replace with your actual API key

# Function to get response using Google Gemini API
def get_response(question):
    # Initialize Google Gemini API with your API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Generate the response using Google Gemini (Gemini-1.5-flash)
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(question)
    return response.text

## Function to set custom CSS for premium aesthetics
def set_premium_css():
    st.markdown(
        """
        <style>
        /* Overall Page Styling */
        body {
            background-color: #000000;
            font-family: 'Arial', sans-serif;
        }

        /* Streamlit Container Styling */
        .stApp {
            background: #000000;
            color: white;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* Clean, Single Input Box */
        input[type="text"] {
            background-color: #1e1e1e !important;  /* Dark background */
            color: #ffffff !important;  /* White text */
            border: 2px solid #006400 !important;  /* Dark green border */
            border-radius: 10px !important;
            padding: 12px 18px !important;
            font-size: 13px !important;
            width: 100% !important;
            margin: 10px auto !important;
            display: block !important;
            text-align: left !important;
        }

        input[type="text"]:focus {
            outline: none !important;
            border: 2px solid #004d00 !important;
            box-shadow: 0 0 6px rgba(0, 77, 0, 0.5) !important;
        }

        /* Remove Extra Containers Affecting Input */
        div[data-testid="stTextInput"] > div {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
        }

        /* Buttons - Vertical Layout */
        .stButton>button {
            background-color: white !important;
            color: #006400 !important;  /* Dark green text */
            border: 2px solid #006400 !important;
            border-radius: 8px !important;
            padding: 12px 18px !important;
            font-size: 14px !important; /* Adjusted font size */
            font-weight: 500 !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out !important;
            width: 100% !important;  /* Full width for vertical alignment */
            margin: 10px 0 !important;  /* Vertical spacing between buttons */
            text-align: center !important;
            box-sizing: border-box;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;  /* Prevents text overflow */
        }

        .stButton>button:hover {
            background-color: #f0f0f0 !important;
            transform: scale(1.03) !important;
        }

        /* Button Container */
        div[data-testid="stButton"] {
            width: 100%;  /* Full width */
            display: block;
        }

        /* Centered message with smaller text */
        .stText {
            font-size: 12px !important;  /* Smaller text size */
            text-align: center !important;  /* Centered text */
            color: #006400 !important;  /* Green text color */
            margin-top: 20px !important;  /* Add margin to space it from other elements */
        }

        /* Custom Green Line Below Output */
        .green-line {
            border: 0;
            height: 2px;
            background-color: #006400 !important;
            width: 100%;
            margin-top: 20px;
        }

        /* Caution message below the green line */
        .caution-text {
            font-size: 10px !important; /* Smaller font size */
            text-align: center !important;
            color: #b3b3b3 !important; /* Light grey color for caution */
            margin-top: 10px !important;
        }

        </style>
        """, unsafe_allow_html=True)


# Initialize Streamlit app
st.set_page_config(page_title="Nexora AI - AI that adapts to industries, providing data-driven decisions for smarter outcomes.", page_icon="🤖")

# Apply Premium CSS
set_premium_css()

# Add a header
# st.header("Nexora AI")

# Insert an image (Update path for your image)
st.image("/Users/likithreddy/Downloads/projects/Q & A bot llm/Black Gold Minimalist Elegant Business LinkedIn Banner/3.png", use_container_width=True)

# Centered message with smaller text (above input box)
st.markdown("<p class='stText'>Type your question and press Enter, or choose an industry for insights.?</p>", unsafe_allow_html=True)

# User input box
input_question = st.text_input("Ask a Question", placeholder="e.g. what type of machines they used in wars?", label_visibility="collapsed")

# Industry buttons for selective answers
col1, col2, col3, col4 = st.columns(4)

with col1:
    healthcare = st.button('Healthcare')
with col2:
    finance = st.button('Finance')
with col3:
    manufacturing = st.button('Manufacturing')
with col4:
    technology = st.button('Technology')

# Generate general insight when user presses Enter
if input_question:
    general_insight = f"give general basic, important info in paras and points based on the question: {input_question}"
    general_response = get_response(general_insight)
    st.subheader("Response:")
    st.write(f"**{general_response}**")
    # Add a green line below the answer
    st.markdown("<hr class='green-line'>", unsafe_allow_html=True)
    # Caution message below the line
    st.markdown("<p class='caution-text'>AI-generated content may contain mistakes. Please verify information carefully.</p>", unsafe_allow_html=True)

# Handle industry button clicks and generate insights
if healthcare:
    healthcare_insight = f"Healthcare industry insights based on the question: {input_question}"
    healthcare_response = get_response(healthcare_insight)
    st.subheader("AI-Powered Healthcare Response:")
    st.write(f"**{healthcare_response}**")

elif finance:
    finance_insight = f"Finance industry insights based on the question: {input_question}"
    finance_response = get_response(finance_insight)
    st.subheader("AI-Powered Finance Response:")
    st.write(f"**{finance_response}**")

elif manufacturing:
    manufacturing_insight = f"Manufacturing industry insights based on the question: {input_question}"
    manufacturing_response = get_response(manufacturing_insight)
    st.subheader("AI-Powered Manufacturing Response:")
    st.write(f"**{manufacturing_response}**")

elif technology:
    technology_insight = f"Technology industry insights based on the question: {input_question}"
    technology_response = get_response(technology_insight)
    st.subheader("AI-Powered Technology Response:")
    st.write(f"**{technology_response}**")

# # Add a section about you at the end
# Add a simple "About Me" section with developer info at the end of the UI
st.markdown("""
    <div style="text-align: center; color: white; font-size: 14px;">
        <p>Developed by Likith, crafted with passion and curiosity.</p>
    </div>
""", unsafe_allow_html=True)
