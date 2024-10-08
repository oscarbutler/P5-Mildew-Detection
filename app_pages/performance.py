import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.evaluate import load_test_evaluation


def performance_function():

    st.title("Performance")

    version = 'v1'
    labels_distribution = plt.imread(f"outputs/{version}/labels_img_distribution.png")

    st.image(labels_distribution,
             caption='Labels on Train, Validation and Test Sets')
    st.info("These two graphs shows the accuracy and losses of the training process.")
    image_model_loss = plt.imread(f"outputs/{version}/model_losses.png")
    st.image(image_model_loss, caption="Model of losses")
    image_model_acc = plt.imread(f"outputs/{version}/model_acc.png")
    st.image(image_model_acc, caption="Model of accuracy")
    st.info("In the dataset that we have received there are:"
    f"train - healthy: 1472 images, train - powdery_mildew: 1472 images"
    f"validation - healthy: 210 images validation - powdery_mildew: 210 images"
    f"test - healthy: 422 images test - powdery_mildew: 422 images")

    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))