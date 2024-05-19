import streamlit as st
from predict1 import show_predict_page
from explore_page import show_explore_page



page = st.sidebar.selectbox("Explore Or predict1", ("predict1", "Explore"))
#show_predict_page()

if page == "predict1":
    show_predict_page()
else:
    show_explore_page()