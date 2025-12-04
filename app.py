import streamlit as st

st.title("simple Devops dashboard")
st.write("This is your version 1.0")

name = st.text_input("Your name here")

if name:
    st.success(f"Hello,{name}")

st.metric("Builds","1")
