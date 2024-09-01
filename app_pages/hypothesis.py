import streamlit as st

def hypothesis_function():

    st.title("Hypothesis")

    st.success(
        f"* Cherry leaves that are affected by powdery mildew will have white spots that appear."
        f"The model that has been created will be able to determine if a leaf is"
        f"healthy or afflicted with powdery mildew."
    )
