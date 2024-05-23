import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import io

def img_to_bytes(img_path, width=300):
    # Ouvrir l'image avec Pillow
    img = Image.open(img_path)
    # Redimensionner l'image en conservant les proportions
    img.thumbnail((width, width))
    # Créer un objet de mémoire en bytes
    img_bytes = io.BytesIO()
    # Enregistrer l'image redimensionnée dans l'objet de mémoire en bytes
    img.save(img_bytes, format='PNG')
    # Récupérer les bytes de l'image redimensionnée
    img_bytes = img_bytes.getvalue()
    # Encoder les bytes en base64
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path, width=300):
    # Appeler img_to_bytes pour obtenir les bytes de l'image redimensionnée
    img_bytes = img_to_bytes(img_path, width)
    # Créer la balise HTML avec l'image redimensionnée
    img_html = "<img src='data:image/png;base64,{}' style='width:{}px;'>".format(
        img_bytes, width)
    return img_html

st.markdown("<h1 style='text-align: center; color: black;'>Welcome to my website 👋🏽</h1>", unsafe_allow_html=True)

st.write("")

st.write("")

st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('assets/profile_picture.png')+"</p>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Dimitri Kneur, Data Analyst</h2>", unsafe_allow_html=True)
