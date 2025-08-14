import streamlit as st
import matplotlib.pyplot as plt
# import plotly.express as px
import numpy as np

# Matplotlib
arr = np.random.normal(1,1, size = 1000)
fig, ax =  plt.subplots()
ax.hist(arr, bins = 30)
plt.grid()
st.pyplot(fig)