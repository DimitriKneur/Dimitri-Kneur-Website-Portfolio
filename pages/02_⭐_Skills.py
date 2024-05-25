import streamlit as st
from PIL import Image
from pathlib import Path
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Dimitri Kneur Website", 
                   page_icon=":rocket:", 
                   layout="wide")

st.header("Skills", divider="red")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

data_collection = load_lottieurl("https://lottie.host/fa5390aa-1e99-487b-982c-425b0397d1f6/rOr7aL5sl1.json")
data_cleaning = load_lottieurl("https://lottie.host/bf3093d4-b637-471e-b737-6e22ab27b09d/2pfA5B7X6E.json")
data_exploration = load_lottieurl("https://lottie.host/d2451c32-0ca1-4422-b015-d28ca22735ae/FAG9Wtf06k.json")
data_visualization = load_lottieurl("https://lottie.host/e81c9f38-e5b6-4e78-ad06-6f54177d3e57/zFw1ZAoWG3.json")

col1, col2, col3, col4 = st.columns((1, 1, 1, 1), gap='large')

with col1:
    st.markdown("<h3 style='text-align: left; '>Data Collection</h3>", unsafe_allow_html=True)
    st_lottie(data_collection, width=180)
    st.markdown("""
    <div style='text-align: justify;'>
        Collecting comprehensive data to conduct insightful analyses is a crucial ability for a Data Analyst. Techniques such as web scraping and using APIs are often involved to gather data from various sources.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style='text-align: justify;'>
        For example, I used both techniques to <a href="https://github.com/DimitriKneur/Retrieve-Artworks-Louvre-using-Scraping-and-API/tree/main" target="_blank">collect data on Louvre Museum artworks</a>.
    </div>
    """, unsafe_allow_html=True)



with col2:
    st.markdown("<h3 style='text-align: left;'>Data Cleaning</h3>", unsafe_allow_html=True)
    st_lottie(data_cleaning, width=180)
    st.markdown("""
    <div style='text-align: justify;'>
        Cleaning data is a fundamental task for a Data Analyst to produce meaningful, accurate and reliable analysis results. It involves handling missing values, removing inaccuracies, and standardizing formats.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style='text-align: justify;'>
        Nearly every data project nowadays involves a data cleaning step.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("<h3 style='text-align: left;'>Data Exploration</h3>", unsafe_allow_html=True)
    st_lottie(data_exploration, width=152)
    st.markdown("""
    <div style='text-align: justify;'>
        Data exploration involves analyzing the characteristics, structure and relationships and  within a dataset. It helps identify patterns, biases, and outliers, laying the groundwork for deeper analysis.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style='text-align: justify;'>
        You can have a look at <a href="https://dimitri-kneur.streamlit.app/Data_Stack" target="_self">my data stack</a> to see which tools I can use to explore data.
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("<h3 style='text-align: center; '>Data Viz.</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st_lottie(data_visualization, width=200)
    st.write("")
    st.write("")
    st.markdown("""
    <div style='text-align: justify;'>
        By creating charts, graphs, and interactive dashboards, analysts can uncover insights, patterns, and trends within the data. Visualization facilitates data-driven decision-making for the stakeholders.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style='text-align: justify;'>
        
    You can explore <a href="https://dimitri-kneur.streamlit.app/Projects" target="_self">my projects</a> to see how I utilize data visualization techniques.
    </div>
    """, unsafe_allow_html=True)