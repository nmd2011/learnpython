import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Todd Groudan")
    content = """
    Hi, I am Todd and am learning Python for fun
    """
    st.info(content)

content1 = "I created some applications for practice.  Please click the link below or email me with any questions"

st.write(content1)

df = pd.read_csv("data.csv", sep=';')

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
