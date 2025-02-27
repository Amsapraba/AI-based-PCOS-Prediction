import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Health Tracking Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "Daily Check-In", "Challenges & Goals", "Leaderboard", "Data Visualization"])

if page == "Home":
    st.title("Welcome to the Health Tracking Game!")
    st.write("Log your health, complete challenges, and earn rewards!")
    
elif page == "Daily Check-In":
    st.title("Daily Health Check-In")
    mood = st.selectbox("How do you feel today?", ["Great", "Okay", "Tired", "Stressed", "Unwell"])
    exercise = st.checkbox("Did you exercise today?")
    sleep = st.slider("Hours of sleep", 0, 12, 7)
    water = st.slider("Glasses of water", 0, 10, 8)
    symptoms = st.text_area("Any symptoms?")
    if st.button("Submit Check-In"):
        st.success("Check-in recorded! Keep up the good habits.")
    
elif page == "Challenges & Goals":
    st.title("AI-Suggested Health Challenges")
    challenges = ["Try a 10-minute meditation session", "Go for a walk", "Drink more water today", "Do some stretching"]
    challenge = np.random.choice(challenges)
    st.write(f"Today's Challenge: {challenge}")
    if st.button("Complete Challenge"):
        st.success("Challenge completed! You've earned 50 points.")
    
elif page == "Leaderboard":
    st.title("Leaderboard & Streaks")
    users = ["Alice", "Bob", "Charlie", "You"]
    points = [300, 250, 200, 150]
    leaderboard = pd.DataFrame({"User": users, "Points": points})
    st.dataframe(leaderboard)
    
elif page == "Data Visualization":
    st.title("Non-Invasive Health Feature Visualization")
    uploaded_file = st.file_uploader("Upload CSV for analysis", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Display available columns
        st.write("Available columns in dataset:", list(df.columns))
        
        # Define possible non-invasive features
        possible_features = ["Age", "BMI", "Blood Pressure", "Heart Rate", "Steps per Day"]
        
        # Find matching columns in uploaded dataset
        available_features = [col for col in possible_features if col in df.columns]
        
        if available_features:
            df = df[available_features].dropna()
            
            st.subheader("Health Trends of Non-Invasive Features")
            fig, ax = plt.subplots(figsize=(10,6))
            sns.boxplot(data=df, ax=ax)
            ax.set_xticklabels(available_features, rotation=45)
            st.pyplot(fig)
            
            st.subheader("Correlation Heatmap of Non-Invasive Features")
            fig, ax = plt.subplots(figsize=(10,6))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.error("No matching non-invasive health features found in the uploaded dataset. Please upload a valid CSV.")
