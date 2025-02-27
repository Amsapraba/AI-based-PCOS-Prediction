import streamlit as st

st.set_page_config(page_title="PCOS ML Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "What is PCOS?"])

if page == "Home":
    st.title("Welcome to Our PCOS ML Game!")
    st.write("Explore PCOS in a fun and interactive way!")
    
elif page == "What is PCOS?":
    st.title("What is PCOS?")
    st.write("Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder in women. It can lead to irregular periods, excessive androgen levels, and ovarian cysts. Early diagnosis and management are crucial.")
