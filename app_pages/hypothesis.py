import streamlit as st

def hypothesis_function():

    st.title("Hypothesis")

    st.success(
        f"* Cherry leaves that are affected by powdery mildew will have white spots that appear."
        f"The model that has been created will be able to determine if a leaf is"
        f"healthy or afflicted with powdery mildew."
        f"The model that has been created will have a 97% success rate at accuratly identifying"
        f"powdery mildew in the leaves."
    )

    st.success(
        f"Through the user of our visualise page we can determine the"
        f"biggest differences between a healthy leaf and an"
        f"infected one."
    )