import streamlit as st

st.title("WIDGETS")
if st.button("on a single click, Jo chahiye vo milega"):
    st.write("tu single hi rahega! :sunglasses:")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter Your address")
st.write(address)

st.date_input("date")
st.time_input("time")
if st.checkbox("You accept the T&C", value=False):
    st.write("thank you")

v1=st.radio("Colours",["r","g","b"],index=1)
v2=st.selectbox("Colours",["r","g","b"],index=0)
st.write(v1,v2)
v3=st.multiselect("Colours",["r","g","b"])
st.write(v3)

age = st.slider("age",min_value=18,max_value=40,value=30,step=2)
st.write(age)
st.number_input("numbers",min_value=18,max_value=40,value=30,step=2)
st.file_uploader("upload a file")