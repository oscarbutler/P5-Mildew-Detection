
import streamlit as st
from app_pages.multipage import MultiPage
st.set_page_config(
    page_title="Mildew Detection",
    page_icon="🖥️"
)
from app_pages.visualiser import visualize_image
from app_pages.performance import performance_function
from app_pages.prediction import detector
from app_pages.summary import summary_function

app = MultiPage(app_name="Powdery Mildew Detector")

app.add_page("Summary", summary_function)
app.add_page("Visualiser", visualize_image)
app.add_page("Prediction", detector)
app.add_page("Hypothesis", hypothesis_function)
app.add_page("Performance", performance_function)

app.run()