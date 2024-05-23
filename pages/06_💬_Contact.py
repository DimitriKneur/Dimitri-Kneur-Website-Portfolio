import streamlit as st
import base64
from pathlib import Path

from PIL import Image
import io

st.set_page_config(page_title="My Portfolio Website", 
                   page_icon=":rocket:", 
                   layout="wide")

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

def img_to_html(img_path, width=222):
    # Appeler img_to_bytes pour obtenir les bytes de l'image redimensionnée
    img_bytes = img_to_bytes(img_path, width)
    # Créer la balise HTML avec l'image redimensionnée
    img_html = "<img src='data:image/png;base64,{}' style='width:{}px;'>".format(
        img_bytes, width)
    return img_html

st.markdown("<h1 style='text-align: center; color: black;'>💬 Contact</h1>", unsafe_allow_html=True)

st.write("")

st.write("")

st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('assets/profile_picture.png')+"</p>", unsafe_allow_html=True)

# Social Icons
social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/dimitri-kneur-audencia/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/DimitriKneur", "https://icon-library.com/images/github-icon-vector/github-icon-vector-0.jpg"]
        }

social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 40px;'></a>" for platform in social_icons_data]

bol1, bol2, bol3 = st.columns(3)
with bol1:
    st.write(' ')
with bol2:
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)
with bol3:
    st.write(' ')

aol1, aol2, aol3 = st.columns(3)
with aol1:
    st.write(' ')

with aol2:
    st.markdown("""
        <div style='text-align: center;'>
            <a href="mailto:dimitri.kneur@protonmail.com">📫 dimitri.kneur@protonmail.com</a>
        </div>
    """, unsafe_allow_html=True)

with aol3:
    st.write(' ')

dol1, dol2, dol3 = st.columns(3)
with dol1:
    st.write(' ')
with dol2:
    st.write("<div style='text-align: center;'>📱 +33 7 65 62 79 91</div>", unsafe_allow_html=True)
with dol3:
    st.write(' ')

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write(' ')