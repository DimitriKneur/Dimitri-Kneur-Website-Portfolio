import streamlit as st

st.title("Welcome to my website 👋🏽")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('assets/profile_picture.png', width=300)

st.write("Dimitri Kneur")

