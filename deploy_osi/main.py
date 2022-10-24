import streamlit as st
import frontend
import backend

navigation= st.sidebar.selectbox('Pilih Halaman : ', ('Exploratory Data Analysis','Predict Online Shopper Intention'))

if navigation=='Exploratory Data Analysis':
    frontend.run()
else:
    backend.run()