import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

st.set_page_config(page_title="Health Tracking Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "Daily Check-In", "Challenges & Goals", "Leaderboard", "Health Assessment", "Symptom-Based AI Prediction", "Health Quiz", "Community Support"])

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
    
elif page == "Symptom-Based AI Prediction":
    st.title("AI Symptom Prediction")
    st.write("Enter your symptoms, and the AI will suggest possible conditions.")
    
    symptom_input = st.text_area("Describe your symptoms (e.g., headache, fever, fatigue)")
    
    if st.button("Predict Condition"):
        example_conditions = {
            "headache fever fatigue": "Possible flu or viral infection",
            "stomach pain nausea": "Possible food poisoning or indigestion",
            "shortness of breath cough": "Possible respiratory infection or asthma",
            "joint pain stiffness": "Possible arthritis or inflammation"
        }
        
        vectorizer = TfidfVectorizer()
        X = list(example_conditions.keys())
        y = list(example_conditions.values())
        X_vectorized = vectorizer.fit_transform(X)
        
        model = MultinomialNB()
        model.fit(X_vectorized, y)
        
        input_vectorized = vectorizer.transform([symptom_input])
        prediction = model.predict(input_vectorized)
        
        st.subheader("Prediction Result")
        st.write(f"The AI suggests: **{prediction[0]}**")
        
        st.success("This is a basic prediction. Consult a doctor for accurate medical advice.")
    
elif page == "Health Quiz":
    st.title("Health Knowledge Quiz")
    st.write("Test your knowledge about health and wellness!")
    
    questions = {
        "What is a normal resting heart rate?": ["60-100 BPM", "30-50 BPM", "120-150 BPM"],
        "Which nutrient is essential for strong bones?": ["Calcium", "Vitamin C", "Iron"],
        "What is the recommended daily water intake?": ["8 glasses", "3 glasses", "15 glasses"]
    }
    
    for q, options in questions.items():
        answer = st.radio(q, options)
        if answer == options[0]:
            st.success("Correct!")
        else:
            st.error("Incorrect, try again!")
    
elif page == "Community Support":
    st.title("Community Support & Discussions")
    st.write("Share your experiences, ask health questions, and support others!")
    
    user_post = st.text_area("Write a post or ask a question")
    if st.button("Post"):
        st.success("Your post has been shared!")
    
    st.subheader("Recent Posts")
    community_posts = [
        "Alice: I’ve been struggling with sleep, any tips?",
        "Bob: What are some healthy meal prep ideas?",
        "Charlie: How do you stay motivated to exercise?"
    ]
    for post in community_posts:
        st.write(post)
