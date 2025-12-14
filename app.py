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

#3. Show dataset
if uploaded_file is not None:
    if st.checkbox("Show dataset summery"):
        if st.button("Head"):
            st.write(df.head())
        if st.button("Tail"):
            st.write(df.tail())
#4. check datatype of each column
if uploaded_file is not None:
    if st.checkbox("show datatype of each column"):
        st.text("Data Types")
        st.write(df.dtypes)
#5. find the shape of the datset


if uploaded_file is not None:
    if st.checkbox("Find the shape of the dataset"):
        data_shape = st.radio("Show Dimension By", ("Rows", "Columns"))
        if data_shape == 'Rows':
            st.write(f"Number of Rows: {df.shape[0]}")
        elif data_shape == 'Columns':
            st.write(f"Number of Columns: {df.shape[1]}")   