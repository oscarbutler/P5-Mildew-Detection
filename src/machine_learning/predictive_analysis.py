import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

def plot_probabilities(probability, prediction_class):

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Parasitised': 0, 'Uninfected': 1}.keys(),
        columns=['Probability']
    )