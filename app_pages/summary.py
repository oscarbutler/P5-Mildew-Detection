import streamlit as st

def summary_function():

    st.title("Summary")

    st.info(
        f"Powdery mildew is a parasitic fungal disease caused by various species. "
        f"It affects a wide range of plants, "
        f"causing white, powdery spots to appear on the leaves, stems, and sometimes "
        f"the fruit of the plant.\n"
        f"As the infection progresses, these spots grow bigger and become so large they combine, "
        f"eventually covering the entire leaf surface."
        f"Powdery mildew thrives in conditions of high humidity and moderate temperatures, "
        f"leading to a lot of damage if apporpriatly dealt with if it is not it can lead to lower crop yields."
    )

    st.success(
        f"We have recieved the dataset which includes 4208 images"
        f"and that it is split equally with 2104 being healthy leaves"
        f"and 2104 being infected leaves."
        f"This can be found at [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )