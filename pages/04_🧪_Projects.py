import streamlit as st

st.set_page_config(page_title="My Portfolio Website", 
                   page_icon=":rocket:")

st.header("Projects", divider="red")

col1, col2 = st.columns((1, 0.86))

with col1:
    st.image("assets/Retail_Dashboard_Snapshot.gif", caption="Interactive Power BI dashboard / Global Electronics Retailer")
    st.image("assets/Netflix_Catalog_Presentation_Snapshot.gif", caption="Analyze the catalog of Netflix with Power BI")

with col2:
    st.image("assets/Demo_streamlit_le_louvre.gif", caption = "Application listing the artworks at the Louvre Museum")
    st.image("assets/World_Population_Evolution_Snapshot.gif", caption="Analyze the world population's evolution (2000 - 2021)")

st.markdown("""
    <p style='text-align: center; color: black;'>
        Do you want to have a closer look at all my projects? 
        Follow this <a href="https://github.com/DimitriKneur/Data-Projects/blob/main/README.md">link</a>.
    </p>
""", unsafe_allow_html=True)