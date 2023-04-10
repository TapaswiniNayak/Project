#app1.py
import streamlit as st
def app():
    new_title = '<p style="font-family:algerian; color:White; font-size: 150px;">HOME</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_rec = '<p style="font-family: Lucida Calligraphy; color:White; font-size: 50px; font-weight: bold;">Best Place To Seek Your Next Movie Venture</p>'
    st.markdown(new_rec, unsafe_allow_html=True)


    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("http://1.bp.blogspot.com/-LlzQBt85_cU/XcuyQWmqXAI/AAAAAAAAAlo/kSfshUvmBL4te1ECbrzWaDL957fZjQKdQCLcBGAsYHQ/s1600/Movierulz.jpg")
        }
        .sidebar .sidebar-content {
            background: url("http://1.bp.blogspot.com/-LlzQBt85_cU/XcuyQWmqXAI/AAAAAAAAAlo/kSfshUvmBL4te1ECbrzWaDL957fZjQKdQCLcBGAsYHQ/s1600/Movierulz.jpg")
        }
        </style>
        """,
        unsafe_allow_html=True
    )