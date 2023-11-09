import streamlit as st

st.title("Welcome to Streamlit")

st.header("Header")

st.subheader("subheader")

st.text("I like You more then You!")

st.markdown("""
# h1 tag
## h2 tag
### h3 tag
### h3 tag<br> new line using br tag
:moon:            
:sunglasses::book: ** bold **                 
""",True)

st.latex(r'''(a+b)^2=a^2+b^2+2ab''')

st.write("roj","marry","marlo")

st.write("# hmmm ")