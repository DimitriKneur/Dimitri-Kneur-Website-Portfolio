import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>Welcome to my website 👋🏽</h1>", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('assets/profile_picture.png', width=300)
st.markdown("<h2 style='text-align: center; color: black;'>Dimitr Kneur, Data Analyst</h2>", unsafe_allow_html=True)
