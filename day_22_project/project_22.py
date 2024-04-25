import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv("data.csv")

st.title("The Best Company Ever")
st.text("""Random thoughts of nothing but how to fill the space in the page and in my head"
        "Hoping this is enough babbling to cover more of the page""")

st.header("THE TEAM")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("imgs/" + row["image"])

    with col2:
        for index, row in df[4:8].iterrows():
            st.subheader(f"{row['first name']} {row['last name']}".title())
            st.write(row["role"])
            st.image("imgs/" + row["image"])

    with col3:
        for index, row in df[8:].iterrows():
            st.subheader(f"{row['first name']} {row['last name']}".title())
            st.write(row["role"])
            st.image("imgs/" + row["image"])
