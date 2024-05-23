import streamlit as st
from pages import 🚀_Projects

# Définir les pages de l'application
def page_home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

# Créer un dictionnaire pour mapper les noms des pages aux fonctions
pages = {
    "Home": page_home,
    "Projects": 🚀_Projects.page_projects
}

# Utiliser un sélecteur dans la barre latérale pour naviguer entre les pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Appeler la fonction de la page sélectionnée
pages[selection]()
