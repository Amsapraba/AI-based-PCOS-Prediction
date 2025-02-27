import streamlit as st

st.set_page_config(page_title="PCOS ML Game", page_icon="✨", layout="centered")

# Page selection
page = st.sidebar.radio("Navigation", ["🏠 Home", "📖 What is PCOS?"])

if page == "🏠 Home":
    st.title("🎮 Welcome to Our ML Game!")
    st.markdown(
        "- 🌟 **Experience an innovative, gamified approach to explore and learn about PCOS.**\n"
        "- 💡 **Engage with our interactive model and uncover insights in a fun way!**"
    )
    if st.button("👉 Learn More"):
        st.session_state["page"] = "📖 What is PCOS?"
        st.experimental_rerun()

elif page == "📖 What is PCOS?":
    st.title("📖 What is PCOS?")
    st.markdown(
        "- 📢 **Polycystic Ovary Syndrome (PCOS) is a hormonal disorder common among women.**\n"
        "- ⚠️ **Causes irregular periods, excessive androgen levels, and polycystic ovaries.**\n"
        "- 🎯 **May lead to metabolic issues, weight gain, and increased diabetes risk.**\n"
        "- 🏥 **Early diagnosis and management can help in treatment.**"
    )
    if st.button("🔙 Back to Home"):
        st.session_state["page"] = "🏠 Home"
        st.experimental_rerun()
