import streamlit as st
from predict_page import show_predict_page
##from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
show_predict_page()
