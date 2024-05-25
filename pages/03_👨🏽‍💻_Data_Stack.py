import streamlit as st
from PIL import Image
from pathlib import Path
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Dimitri Kneur Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Data Stack", divider="red")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/c0d44f88-bdec-4742-a340-3ac8b2713ff2/Ey6hjgNcgw.json")

col1, col2, col3 = st.columns((1, 1, 1))

with col1:
    st.write(' ')

with col2:
    st_lottie(lottie_coder, width=200)

with col3:
    st.write(' ')

def txt3(a, b):
  col1, col2 = st.columns([2,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

txt3("Programming Languages","`Python`, `SQL`")
txt3("IDE","`Visual Studio Code`")
txt3("Python Libraries & Frameworks","`pandas`, `plotly`, `scrapy`, `streamlit`, `Numpy`, `Matplotlib`, `Seaborn`, `requests`")
txt3("Data Sources","`Hubspot`, `Microsoft Azure`, `Amazon S3`")
txt3("Databases","`MySQL`, `Azure Data Studio`, `Amazon RDS`")
txt3("Data Lakes / Warehouses","`BigQuery`, `Snowflake`")
txt3("ELT & Data Transformation","`Fivetran`, `dbt`")
txt3("Data Visualization Tools","`Power BI`, `Looker Studio`, `Dataiku`, `Excel`")