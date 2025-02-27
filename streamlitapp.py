import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Health Tracking Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "Daily Check-In", "Challenges & Goals", "Leaderboard", "Data Visualization", "Health Prediction"])

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
    st.title("Health Data Visualization")
    uploaded_file = st.file_uploader("Upload CSV for analysis", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Health Trends")
        fig, ax = plt.subplots()
        sns.lineplot(data=df, ax=ax)
        st.pyplot(fig)
    
elif page == "Health Prediction":
    st.title("AI-Based Health Prediction")
    scaler = MinMaxScaler()
    
    def build_lstm_model(input_shape):
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=input_shape),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(25, activation='relu'),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    if st.button("Predict Health Trends"):
        data = np.random.rand(100, 1)
        data_scaled = scaler.fit_transform(data)
        X = np.array([data_scaled[i-10:i] for i in range(10, len(data_scaled))])
        y = data_scaled[10:]
        model = build_lstm_model((X.shape[1], X.shape[2]))
        model.fit(X, y, epochs=10, batch_size=16, verbose=0)
        future_prediction = model.predict(X[-1].reshape(1, X.shape[1], X.shape[2]))
        st.write(f"Predicted Health Score: {future_prediction[-1][0]:.2f}")
        
        if future_prediction[-1] > 0.7:
            st.write("AI Suggestion: Focus on relaxation today!")
        elif future_prediction[-1] < 0.3:
            st.write("AI Suggestion: Keep up the good work!")
        else:
            st.write("AI Suggestion: Maintain your current routine.")
