#app.py
import app1
import dataset
import streamlit as st
PAGES = {
    "Home": app1,
    "Recommender": dataset
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
pages = PAGES[selection]
page.app()