import streamlit as st


def detector():

    image_input = st.file_uploader('Upload Image of Leaf' type='PNG', accept_multiple_files=True)