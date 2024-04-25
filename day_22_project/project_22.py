import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

print(df)

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.write(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row["image"])

    with col2:
        for index, row in df[4:8].iterrows():
            st.write(f"{row['first name']} {'last name'}")

    with col3:
        for index, row in df[8:].iterrows():
            st.write(f"{row['first name']} {'last name'}")




