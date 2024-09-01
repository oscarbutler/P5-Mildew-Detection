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