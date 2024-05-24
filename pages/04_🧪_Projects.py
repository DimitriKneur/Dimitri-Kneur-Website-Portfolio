import streamlit as st

st.set_page_config(page_title="My Portfolio Website", 
                   page_icon=":rocket:",
                   layout="wide")

st.header("Projects", divider="red")

st.markdown("""
    <h3 style='text-align: center; color: black;'>
        ¤
        <a href="https://github.com/DimitriKneur/Global-Electronics-Retailer-Analysis">
            Interactive Power BI sales dashboard
        </a>
    </h3>
    """, unsafe_allow_html=True)


col1, col2, col3 = st.columns((1, 3.2, 1))

with col1:
    st.write(' ')

with col2:
    st.image("assets/Retail_Dashboard_Snapshot.gif")

with col3:
    st.write(' ')

st.write(' ')

st.markdown("""<h3 style='text-align: center; color: black;'>¤ <a href="https://github.com/DimitriKneur/Netflix-Catalog-Analysis-PowerBI">Analysis of the catalog of Netflix with Power BI</a></h3>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 3.2, 1))

with col1:
    st.write(' ')

with col2:
    st.image("assets/Netflix_Catalog_Presentation_Snapshot.gif")

with col3:
    st.write(' ')

st.write(' ')

st.markdown("""<h3 style='text-align: center; color: black;'>¤ <a href="https://github.com/DimitriKneur/World-Population-Evolution-Project/tree/main">Analysis of the world population's evolution</a></h3>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 3.2, 1))

with col1:
    st.write(' ')

with col2:
    st.image("assets/World_Population_Evolution_Snapshot.gif")

with col3:
    st.write(' ')

st.write(' ')

st.markdown("""<h3 style='text-align: center; color: black;'>¤ <a href="https://github.com/DimitriKneur/Le-Louvre-works-of-art-on-display/tree/main">Application listing the artworks at the Louvre Museum</a></h3>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 3.2, 1))

with col1:
    st.write(' ')

with col2:
    st.image("assets/Demo_streamlit_le_louvre.gif")

with col3:
    st.write(' ')

st.write(' ')

st.markdown("""
    <h3 style='text-align: center; color: black;'>
        Do you want to have a closer look at all my projects? 
        Follow this <a href="https://github.com/DimitriKneur/Data-Projects/blob/main/README.md">link</a>.
    </h3>
""", unsafe_allow_html=True)