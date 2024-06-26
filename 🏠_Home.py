import streamlit as st
import base64
from pathlib import Path

from PIL import Image
import io

st.set_page_config(page_title="Dimitri Kneur Website", 
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

def img_to_html(img_path, width=200):
    # Appeler img_to_bytes pour obtenir les bytes de l'image redimensionnée
    img_bytes = img_to_bytes(img_path, width)
    # Créer la balise HTML avec l'image redimensionnée
    img_html = "<img src='data:image/png;base64,{}' style='width:{}px;'>".format(
        img_bytes, width)
    return img_html

st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('assets/profile_picture.png')+"</p>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Dimitri Kneur, Data Analyst</h2>", unsafe_allow_html=True)

# Custom CSS for container
st.markdown("""
    <style>
    .custom-container {
        width: 70%;
        margin: auto;
        border: 1px solid #e6e6e6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Add content to the container
st.markdown("""
    <div class="custom-container">
        <p>👋🏽 Hello! I am Dimitri Kneur, a Data Analyst with 3 years of experience in audit and management control. I have mastered SQL, Python, Power BI, and many other tools through an intensive training program. I am now ready to put my analytical skills to work for a data-driven company.</p>
    </div>
    """, unsafe_allow_html=True)

st.write(' ')

# Social Icons
social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/dimitri-kneur-audencia/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/DimitriKneur", "https://icon-library.com/images/github-icon-white/github-icon-white-5.jpg"]
        }

social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 40px;'></a>" for platform in social_icons_data]

with open("assets/DimitriKneur_CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

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

with col2:
    st.markdown("""
        <div style='text-align: center;'>
            <a href="data:application/pdf;base64,{0}" download="DimitriKneur_CV.pdf">
                <button style="padding: 10px 20px;">📄 Download my CV</button>
            </a>
        </div>
    """.format(base64.b64encode(pdf_bytes).decode()), unsafe_allow_html=True)

with col3:
    st.write(' ')