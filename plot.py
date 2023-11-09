import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
data=pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

plt.scatter(data['a'],data['b'])
st.pyplot()

chart = alt.Chart(data).mark_circle().encode(
    x='a',y='b',tooltip=['a','b']
)
st.altair_chart(chart,use_container_width=True)

st.graphviz_chart("""
digraph{
    watch->like
    like->share
    share->subscribe
    share->watch
}
""")

st.image("data//graph (6).png")
st.audio("data//Pinky blinders no copyringht.mp3")