import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dimitri Kneur Website", 
                   page_icon=":rocket:",
                   layout="wide")

st.header("Projects", divider="red")

st.write(' ')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Power BI Interactive Sales Dashboard', 'Power BI Netflix Catalog Analysis', "World Population's Evolution", 'Le Louvre Museum Artworks Application'],
        orientation = 'horizontal',
        icons = ['clipboard2-data-fill', 'film', 'graph-up', 'table']
    )

if selected == 'Power BI Interactive Sales Dashboard':
    
    image_column, text_column = st.columns((2.42,3), gap='medium')
    with image_column:
        st.write('')
        st.image("assets/Retail_Dashboard_Snapshot.gif")

    with text_column:
        st.write("### [Interactive Power BI Sales Dashboard](https://github.com/DimitriKneur/Global-Electronics-Retailer-Analysis)")
        st.write("##### Analysis of the sales of a global electronics retailer.")
        st.write("- Design a sales overview of sales and order numbers in 2019 vs in 2018  \n- Identify top countries, product categories and brands by sales amounts  \n- Calculate the online sales part among total sales  \n- Highlight the relationship hetween sales, profit, orders and quantity sold  \n- Make a detailed sales report by store with extended filtering possibilities  \n- Split the total number of customers by age category, gender and geo. area")


if selected == 'Power BI Netflix Catalog Analysis':
    
    image_column, text_column = st.columns((2.42,3), gap='medium')
    with image_column:
        st.write('')
        st.image("assets/Netflix_Catalog_Presentation_Snapshot.gif")

    with text_column:
        st.write("### [Power BI Netflix Catalog Analysis](https://github.com/DimitriKneur/Netflix-Catalog-Analysis-PowerBI)")
        st.write("##### Analysis of the catalog of Netflix with Power BI.")
        st.write("- Extract the main statistics about the dataset  \n- Identify which genres are the most present on the platform  \n- Identify in how many countries Netflix is available  \n- Identify which country has the most content  \n- Identify dominant genre per country  \n- Identify if there are seasonality in the catalogue release")


if selected == "World Population's Evolution":
    
    image_column, text_column = st.columns((2.42,3), gap='medium')
    with image_column:
        st.write('')
        st.image("assets/World_Population_Evolution_Snapshot.gif")

    with text_column:
        st.write("### [World Population's Evolution](https://github.com/DimitriKneur/World-Population-Evolution-Project/tree/main)")
        st.write("##### Analysis of the world population's evolution.")
        st.write("- Highlight the global trend of world population's evolution through the years  \n- Identify which are the reasons for this evolution  \n- Understand the birth rate drivers  \n- Understand the death rate drivers  \n- Compare the population's evolution by geographic area  \n- Show the impact of this evolution on the population's demographic structure")


if selected == 'Le Louvre Museum Artworks Application':

    image_column, text_column = st.columns((2.42,3), gap='medium')
    with image_column:
        st.write('')
        st.image("assets/Demo_streamlit_le_louvre.gif")

    with text_column:
        st.write("### [Le Louvre Museum Artworks Application](https://github.com/DimitriKneur/Le-Louvre-works-of-art-on-display/tree/main)")
        st.write("##### Application listing the artworks at the Louvre Museum.")
        st.write('Using scraping techniques and an API, I recreated the database of works of art at the Musée du Louvre in Paris. If you want to see how I collected the necessary data thanks to these techniques, you can follow [this link](https://github.com/DimitriKneur/Retrieve-Artworks-Louvre-using-Scraping-and-API).')
        st.write("I then created a Streamlit application that allows one to see the works currently on display. For each artwork, you will have a snapshot, the creation start date and end date, the creator's name (if applicable), the corresponding collection name, and a direct link to retrieve more information about the artwork. You can explore the application by yourself by following [this link](https://dimitri-kneur-le-louvre-works-of-art-on-display.streamlit.app/).")


st.write(' ')

st.write(' ')

st.markdown("""
        <h4 style='text-align: center;'>
            Do you want to have a closer look at all my projects? 
            Follow this <a href="https://github.com/DimitriKneur/Data-Projects/blob/main/README.md">link</a>.
        </h4>
    """, unsafe_allow_html=True)