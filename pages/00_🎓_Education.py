import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Dimitri Kneur Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Education", divider="red")

jedha = Image.open("assets/logo-jedha-footer.png")
audencia = Image.open("assets/audencia_bs.png")

with st.container():

    st.write("")

    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(jedha, width=120)

    with text_column:
        st.write("### Fullstack Data Analyst Bootcamp, [_Jedha_](https://www.jedha.co/) (2023 - 2024)")
        st.write("##### Main course: Power BI, SQL, Python")
        st.write("**Relevant Coursework:** Python programming, Exploratory Data Analysis, Data Collection, SQL, Power BI, Data Marketing....")

    st.write("")

    image_column2, text_column2 = st.columns((1,5))
    with image_column2:
        st.write("")
        st.write("")
        st.write("")
        st.image(audencia, width=170)

    with text_column2:
        st.write("### Master's Degree in Business Administration, [_Audencia_](https://www.audencia.com/) (2015 - 2019)")
        st.write("##### Main course: Corporate Finance")
        st.write("**Relevant Coursework:** Management Control, Financial Analysis, Cash Management and Derivatives, Portfolio management....")

st.write("")

st.markdown("""
    <div style='text-align: left;'>
        
    See also <a href="https://dimitri-kneur.streamlit.app/Diploma_And_Certifications" target="_self">my diploma and certifications</a>.
    </div>
    """, unsafe_allow_html=True)