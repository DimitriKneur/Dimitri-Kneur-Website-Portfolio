import streamlit as st
import base64
from pathlib import Path

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

st.markdown("<h1 style='text-align: center; color: black;'>Welcome to my website 👋🏽</h1>", unsafe_allow_html=True)

'''st.write("")

st.write("")

st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('assets/profile_picture.png')+"</p>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Dimitri Kneur, Data Analyst</h2>", unsafe_allow_html=True)'''