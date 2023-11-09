import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("ggplot")
data={
    "number":[x for x in range (1,11)],
    "square":[x**2 for x in range (1,11)],
    "twice":[x*2 for x in range (1,11)],
    "thrice":[x*3 for x in range (1,11)]
}

rad = st.sidebar.radio("Navigation",["Home","About us"])

if rad == "Home":
    df = pd.DataFrame(data=data)
    col= st.sidebar.selectbox("Select a Column ",df.columns)
    plt.plot(df["number"],df[col])
    st.pyplot()

if rad == "About us":
    st.write("about us")
    st.error("Error")
    st.success("show success")
    st.info("information")
    st.exception(RuntimeError("run time error"))
    st.warning("this is a warning")

