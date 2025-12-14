# imports
 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1. Title and Subheader
st.title("Data Analysis Dashboard")
st.subheader("Data Analysis using python and streamlit") 

#2.Upload Dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)