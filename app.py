import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.visualiser import visualize_image
from app_pages.performance import performance_function
from app_pages.prediction import detector
from app_pages.summary import summary_function

app = MultiPage(app_name="Powdery Mildew Detector")

app.add_page()
app.add_page()
app.add_page()