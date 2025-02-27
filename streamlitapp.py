import streamlit as st

st.set_page_config(page_title="PCOS ML Game", page_icon="✨", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📖 What is PCOS?"])

if page == "🏠 Home":
    st.title("🎮 Welcome to Our PCOS ML Game!")
    st.markdown(
        "- 🚀 **Explore PCOS in a fun and interactive way!**\n"
        "- 🧠 **Engage with our AI model and gain insights.**\n"
        "- 🎯 **Make learning about PCOS an exciting experience!**"
    )
    st.image("https://source.unsplash.com/800x400/?health,technology", caption="An Innovative Approach to Health Awareness", use_column_width=True)
    
elif page == "📖 What is PCOS?":
    st.title("📖 What is PCOS?")
    st.markdown(
        "- 📢 **Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder in women.**\n"
        "- ⚠️ **Leads to irregular periods, excessive androgen levels, and ovarian cysts.**\n"
        "- 🎯 **Can cause metabolic issues, weight gain, and increased diabetes risk.**\n"
        "- 🏥 **Early diagnosis and management are crucial.**"
    )
    st.image("https://source.unsplash.com/800x400/?health,women", caption="Understanding PCOS", use_column_width=True)
