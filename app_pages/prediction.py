import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

st.info('This page will give us the information on whether we can determine if a leaf is healthy or got powdered mildew.')

def detector():

    image_input = st.file_uploader('Upload Image of Leaf', type='PNG', accept_multiple_files=True)

