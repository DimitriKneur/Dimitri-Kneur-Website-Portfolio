import streamlit as st
import os

# Define the path to your CSS file
css_file_path = "styles.css"

# Function to load the CSS file and inject it into the app
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
load_css(css_file_path)

st.title("Home Page")
st.write("Welcome to the home page!")

