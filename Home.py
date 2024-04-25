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

col3, col4, col5 = st.columns([1.0, 0.5, 1.0])

content2 = "Here are some apps I created"
st.write(content2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
