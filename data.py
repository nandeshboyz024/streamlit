import streamlit as st
import numpy as np
import pandas as pd

a  = [1,2,3,4,5,6,7,8]
n=np.array(a)
nd = n.reshape((2,4))
d={
    "name":["harsh","harshita"],
    "age":[21,18],
    "city":["noida","delhi"]
}
data = pd.read_csv("data//Salary_Data.csv")
#print(data)

st.dataframe(nd)
st.dataframe(d)
st.dataframe(data,width=600,height=600)
st.table(data)
st.table(a)
st.json(d)