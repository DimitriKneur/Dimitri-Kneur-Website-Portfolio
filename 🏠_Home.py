import streamlit as st

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.title("Welcome to my website 👋🏽")
    st.image('assets/profile_picture.png', width=300)
    st.write("Dimitri Kneur")