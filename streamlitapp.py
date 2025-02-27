import streamlit as st
import random
import time
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="PCOS Health Dashboard", page_icon="🩺", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["PCOS Prediction Game", "Risk Meter", "Community Forum", "Personality Quiz"])

# Load and prepare dataset
file_path = "PCOS_data.csv"
def load_data():
    try:
        df = pd.read_csv(file_path)
        df_cleaned = df.drop(columns=["Sl. No", "Patient File No.", "Unnamed: 44"], errors="ignore")
        for col in df_cleaned.columns:
            if df_cleaned[col].dtype == "object":
                df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
            else:
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
        df_cleaned = df_cleaned.apply(pd.to_numeric, errors="coerce")
        return df_cleaned
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

df = load_data()
if df is not None and "PCOS (Y/N)" in df.columns:
    X = df.drop(columns=["PCOS (Y/N)"])
    y = df["PCOS (Y/N)"]
    X_train, X_test, y_train, y_test = train_test_split(X.fillna(X.median()), y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    st.sidebar.write(f"✅ Model Accuracy: {accuracy_score(y_test, model.predict(X_test)) * 100:.2f}%")

# PCOS Prediction Game
if page == "PCOS Prediction Game":
    st.title("🎮 PCOS Prediction Game")
    st.write("Answer the following questions and unlock insights! 🎯")
    user_input = []
    progress_bar = st.progress(0)
    for idx, feature in X.columns:
        value = st.number_input(f"Enter your {feature}", min_value=0.0, format="%.2f")
        user_input.append(value)
        progress_bar.progress((idx + 1) / len(X.columns))
    if st.button("🎲 Predict PCOS Risk!"):
        with st.spinner("Analyzing your data...🔍"):
            time.sleep(2)
            prediction = model.predict(np.array(user_input).reshape(1, -1))
            risk_level = random.randint(1, 100)
        st.success(f"✅ Low risk of PCOS. Your estimated risk level: {risk_level}%" if prediction[0] == 0 else "⚠️ High risk detected! Consult a doctor.")

# Risk Meter
elif page == "Risk Meter":
    st.title("📊 PCOS Risk Meter")
    score = random.randint(0, 100)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "PCOS Risk Level"},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "red" if score > 70 else "orange" if score > 40 else "green"}}
    ))
    st.plotly_chart(fig)

# Community Forum
elif page == "Community Forum":
    st.title("🌍 PCOS Community Forum")
    if "posts" not in st.session_state:
        st.session_state.posts = []
    user_message = st.text_area("Share your experience or ask a question:")
    if st.button("Post"):
        st.session_state.posts.append(user_message)
        st.success("✅ Post shared successfully!")
    st.markdown("### Community Posts")
    for post in reversed(st.session_state.posts):
        st.markdown(f"- {post}")

# Personality Quiz
elif page == "Personality Quiz":
    st.title("🩺 PCOS Lifestyle Risk Assessment")
    questions = {
        "How often do you exercise?": {"Daily": 0, "3-5 times a week": 10, "1-2 times a week": 20, "Rarely": 30},
        "How would you rate your diet?": {"Excellent": 0, "Good": 10, "Average": 20, "Poor": 30},
    }
    score = 0
    for q, options in questions.items():
        answer = st.radio(q, list(options.keys()))
        score += options[answer]
    st.subheader(f"📊 Your PCOS Risk Score: **{score}**")
