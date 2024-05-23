import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>Welcome to my website 👋🏽</h1>", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('assets/profile_picture.png', width=300)


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.write("With a Master's degree in Corporate Finance and solid experience in management control,\n")
    st.write("I Have decided to acquire new skills in the field of data analysis.\n")
    st.write("After an intensive training in a specialized bootcamp, I'm now ready \n")
    st.write("to use my analytical skills in a data-driven environment.")