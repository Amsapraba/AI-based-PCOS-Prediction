import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PCOS ML Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "What is PCOS?", "PCOS Dataset", "Data Visualization"])

if page == "Home":
    st.title("Welcome to Our PCOS ML Game!")
    st.write("Explore PCOS in a fun and interactive way!")
    
elif page == "What is PCOS?":
    st.title("What is PCOS?")
    st.write("Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder in women. It can lead to irregular periods, excessive androgen levels, and ovarian cysts. Early diagnosis and management are crucial.")
    
    st.subheader("Symptoms:")
    st.markdown("- Irregular periods")
    st.markdown("- Excessive hair growth (hirsutism)")
    st.markdown("- Acne and oily skin")
    st.markdown("- Weight gain and difficulty losing weight")
    st.markdown("- Thinning hair or hair loss")
    st.markdown("- Fertility issues")
    
    st.subheader("Causes:")
    st.markdown("- Genetic factors")
    st.markdown("- Insulin resistance")
    st.markdown("- Excess androgen production")
    st.markdown("- Lifestyle and environmental factors")
    
    st.subheader("Effects:")
    st.markdown("- Increased risk of type 2 diabetes")
    st.markdown("- High blood pressure and heart disease")
    st.markdown("- Depression and anxiety")
    st.markdown("- Sleep apnea")
    st.markdown("- Infertility or complications in pregnancy")
    
    st.subheader("Precautions & Management:")
    st.markdown("- Maintaining a healthy diet and regular exercise")
    st.markdown("- Managing stress levels")
    st.markdown("- Consulting a healthcare provider for medical treatments")
    st.markdown("- Monitoring weight and hormone levels")

elif page == "PCOS Dataset":
    st.title("PCOS Dataset")
    st.write("Upload the dataset to view the complete data.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

elif page == "Data Visualization":
    st.title("Data Visualization")
    st.write("Explore key insights from the dataset through visualizations.")
    
    uploaded_file = st.file_uploader("Upload CSV file for visualization", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("Distribution of PCOS Cases")
        fig, ax = plt.subplots()
        sns.countplot(x='PCOS (Y/N)', data=df, ax=ax)
        st.pyplot(fig)
        
        st.subheader("BMI Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['BMI'], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
        
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(df.corr(), annot=False, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
