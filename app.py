import pandas as pd
import streamlit as st

st.markdown("<h1 style='text-align: center;'>LeapCode 踊</h1>", unsafe_allow_html=True)

df = pd.read_csv('./Database/database.csv')

k=st.text_input("Enter the serial number of the problem:")

if k:
    k=int(k)
    st.code(df['Answer'][list(df['Question']).index(k)] , language='c++')
    st.balloons()
