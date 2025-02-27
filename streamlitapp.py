import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Health Tracking Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "Daily Check-In", "Challenges & Goals", "Leaderboard", "Health Assessment"])

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
    
elif page == "Health Assessment":
    st.title("Health Level Assessment")
    st.write("Enter your non-invasive health details to analyze your health level.")
    
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    blood_pressure = st.number_input("Blood Pressure (Systolic)", min_value=80, max_value=180, value=120)
    heart_rate = st.number_input("Heart Rate (BPM)", min_value=40, max_value=150, value=70)
    steps = st.number_input("Steps per Day", min_value=0, max_value=30000, value=5000)
    
    if st.button("Analyze Health"):
        health_data = pd.DataFrame({
            "Feature": ["Age", "BMI", "Blood Pressure", "Heart Rate", "Steps per Day"],
            "Value": [age, bmi, blood_pressure, heart_rate, steps]
        })
        
        st.subheader("Your Health Levels")
        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(x=health_data["Feature"], y=health_data["Value"], palette="coolwarm", ax=ax)
        ax.set_xticklabels(health_data["Feature"], rotation=45)
        st.pyplot(fig)
        
        st.success("Health assessment completed! Keep tracking your health for improvements.")
