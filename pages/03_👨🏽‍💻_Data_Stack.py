import streamlit as st
from PIL import Image
from pathlib import Path
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Portfolio Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Data Stack", divider="red")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/c0d44f88-bdec-4742-a340-3ac8b2713ff2/Ey6hjgNcgw.json")
st_lottie(lottie_coder, width=200)