import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="My Portfolio Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Diploma And Certifications", divider="red")

st.markdown("<h2 style='text-align: center; color: black;'>👨🏾‍🎓 Diploma</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 1, 1))

with col1:
    st.write(' ')

with col2:
    st.image("assets/Diplome.png", caption="Audencia Business School Diploma")

with col3:
    st.write(' ')


st.markdown("<h2 style='text-align: center; color: black;'>🥇 Certifications</h2>", unsafe_allow_html=True)

bol1, bol2, bol3, bol4 = st.columns((1, 1, 1, 1))

with bol1:
    st.image("assets/Google_analytics_certificate_Dimitri_Kneur.png", caption="Google Analytics Certificate")

with bol2:
    st.image("assets/Jedha_fullstack_certification_Dimitri_Kneur.png", caption="Jedha FullStack Data Analysis")

with bol3:
    st.image("assets/Dataiku_certificate_Dimitri_Kneur.png", caption="Dataiku Certificate")

with bol4:
    st.image("https://hubspot-credentials-na1.s3.amazonaws.com/prod/badges/user/164c5f4d8b48434dab5be47d14765f0e.png", caption="Hubspot Certificate")