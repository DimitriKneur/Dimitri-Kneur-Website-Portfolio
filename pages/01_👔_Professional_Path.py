import streamlit as st
from PIL import Image
from pathlib import Path
import base64

st.set_page_config(page_title="Dimitri Kneur Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Professional Path", divider="red")

jedha = Image.open("assets/logo-jedha-footer.png")
audencia = Image.open("assets/audencia_bs.png")
sideme = Image.open("assets/sideme.jpg")
mediapost = Image.open("assets/mediapost.jpg")
mazars = Image.open("assets/mazars.png")

with st.container():

    st.write("")

    image_column, text_column = st.columns((1,5))
    with image_column:
        st.write("")
        st.image(jedha, width=120)

    with text_column:
        st.write("### Teacher Assistant - Data Analysis")
        st.write("##### [_Jedha_](https://www.jedha.co/) | From 2024 | Paris, France")
        st.write("""¤ Lead and supervise tutorial sessions in the 'Fullstack Data Analysis' program  \n¤ Contribute to the continuous improvement of course content and program exercises""")

    st.write("")

    image_column6, text_column6 = st.columns((1,5))
    with image_column6:
        st.image(jedha, width=120)

    with text_column6:
        st.write("### Fullstack Data Analyst Bootcamp")
        st.write("##### [_Jedha_](https://www.jedha.co/) | 2023 - 2024 | Paris, France")
        st.write("**Main course:** Power BI, SQL, Python")

    st.write("")

    image_column3, text_column3 = st.columns((1,5))
    with image_column3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(mediapost, width=120)

    with text_column3:
        st.write("### Management Controller - Data & Digital Activities")
        st.write("##### [_Mediapost_](https://www.mediaposte.fr/) | 2023 | Montrouge, France")
        st.write(""" ¤ Prepare monthly summary dashboards for the Data & Digital scope (€36M)  \n¤ Contribute to annual budget creation and monitoring for Data & Digital  \n¤ Conduct various analyses: client margin, profitability analysis, segment trends...""")

    st.write("")

    image_column3, text_column3 = st.columns((1,5))
    with image_column3:
        st.write("")
        st.write("")
        st.image(sideme, width=120)

    with text_column3:
        st.write("### Management Controller")
        st.write("##### [_Sideme_](http://www.sideme.fr/index.html) | 2021 - 2023 | Levallois-Perret, France")
        st.write(""" ¤ Establish and track performance indicators for the SIDEME scope (€80M)  \n¤ Contribute to cash management and financing optimization  \n¤ Maintain the SAP knowledge base (transactions and instructions)""")

    st.write("")

    image_column3, text_column3 = st.columns((1,5))
    with image_column3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(mazars, width=120)

    with text_column3:
        st.write("### Financial Auditor - Industry and Social Housing")
        st.write("##### [_Mazars_](https://www.mazars.fr/) | 2019 - 2020 | Le Lamentin, Martinique")
        st.write(""" ¤ Perform cut-off, accuracy, and completeness procedures  \n¤ Map risks associated with the operations of client companies  \n¤ Assess the quality of accounting data and internal control of client companies""")

    st.write("")

    image_column2, text_column2 = st.columns((1,5))
    with image_column2:
        st.write("")
        st.write("")
        st.write("")
        st.image(audencia, width=170)

    with text_column2:
        st.write("### Master's Degree in Business Administration")
        st.write("##### [_Audencia_](https://www.audencia.com/) | 2015 - 2019 | Nantes, France")
        st.write("**Main course:** Corporate Finance")

st.write(' ')

with open("assets/DimitriKneur_CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

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