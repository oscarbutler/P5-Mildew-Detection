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

    prob_per_class.loc[prediction_class] = probability
    for x in prob_per_class.index.to_list():
        if x not in prediction_class:
            prob_per_class.loc[x] = 1 - probability
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)

def resize_input_image(img, version):

    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image