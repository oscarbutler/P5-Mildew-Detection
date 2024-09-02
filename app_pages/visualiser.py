import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def visualize_image():
    st.title('Visualiser')

    version = 'v1'

    average_parasite = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
    average_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
    average_difference = plt.imread(f"outputs/{version}/avg_diff.png")

    st.info("This shows the difference between the average powdery mildew and healthy leaves.")

    st.image(average_parasite, caption="Average Of Powdery Mildew Leaves")
    st.image(average_healthy, caption="Averages Of Healthy Leaves")
    st.image(average_difference, caption="The average difference")


    if st.checkbox("Image Montage"): 
      cherry_leaves_dir = 'inputs/cherry-leaves'
      labels = os.listdir(cherry_leaves_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create The Montage"):      
        image_montage(dir_path= cherry_leaves_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=6, ncols=3, figsize=(10,20))

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):

    labels = os.listdir(dir_path)

    images = os.listdir(dir_path+'/' + label_to_display)
    if nrows * ncols < len(images):
      img_index = random.sample(images, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You attempted to create a montage with {nrows * ncols} spaces")
      return

    list_of_rows= range(0,nrows)
    list_of_cols= range(0,ncols)
    plot_index = list(itertools.product(list_of_rows,list_of_cols))

    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_index[x])
      img_shape = img.shape
      axes[plot_index[x][0], plot_index[x][1]].imshow(img)
      axes[plot_index[x][0], plot_index[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_index[x][0], plot_index[x][1]].set_xticks([])
      axes[plot_index[x][0], plot_index[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)