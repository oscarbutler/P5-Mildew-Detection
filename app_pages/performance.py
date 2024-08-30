import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.evaluate import load_test_evaluation


def performance_function():
    version = v1
    labels_distribution = plt.imread(f"outputs/{version}/labels_img_distribution.png")

    st.image(labels_distribution,
             caption='Labels on Train, Validation and Test Sets')
    st.info("These two graphs shows the accuracy and losses of the training process.")
    image_model_loss = plt.imread(f"outputs/{version}/model_losses.png")

    image_model_acc = plt.imread(f"outputs/{version}/model_acc.png")