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

# Social Icons
social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/e-domingo", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/enricd", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Twitter": ["https://twitter.com/mad_enrico", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
        "YouTube": ["https://www.youtube.com/@enricd", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
        "Medium": ["https://medium.com/@enricdomingo", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"]
    }
