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

# Load and clean dataset
file_path = "PCOS_data.csv"

try:
    df = pd.read_csv(file_path)
    df_cleaned = df.drop(columns=["Sl. No", "Patient File No.", "Unnamed: 44"], errors="ignore")

    # Fill missing values
    for col in df_cleaned.columns:
        if df_cleaned[col].dtype == "object":
            df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
        else:
            df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

    df_cleaned = df_cleaned.apply(pd.to_numeric, errors="coerce")

    if "PCOS (Y/N)" not in df_cleaned.columns:
        st.error("Target column 'PCOS (Y/N)' not found in dataset!")
        st.stop()

    X = df_cleaned.drop(columns=["PCOS (Y/N)"])
    y = df_cleaned["PCOS (Y/N)"]

    X.fillna(X.median(), inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    model_accuracy = accuracy_score(y_test, y_pred)
    st.sidebar.write(f"✅ Model Accuracy: {model_accuracy * 100:.2f}%")

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "PCOS Prediction Game", "Community Forum", "Lifestyle Quiz"])

# Home Section
if page == "Home":
    st.title("🏥 PCOS Prediction Dashboard")
    st.write("Welcome to the PCOS Prediction App! Navigate through the sidebar to explore features.")

# PCOS Prediction Game
elif page == "PCOS Prediction Game":
    st.title("🎮 PCOS Prediction Game")
    st.write("Enter your details to predict your PCOS risk.")

    user_input = []
    progress_bar = st.progress(0)

    for idx, feature in enumerate(X.columns):
        value = st.number_input(f"Enter your {feature}", min_value=0.0, format="%.2f")
        user_input.append(value)
        progress_bar.progress((idx + 1) / len(X.columns))

    if st.button("🎲 Predict PCOS Risk!"):
        with st.spinner("Analyzing your data...🔍"):
            time.sleep(2)
            user_input = np.array(user_input).reshape(1, -1)
            prediction = model.predict(user_input)
            risk_level = random.randint(1, 100)

        if prediction[0] == 0:
            st.success(f"✅ Low risk of PCOS. Estimated risk: {risk_level}%")
        else:
            st.warning(f"⚠️ High risk of PCOS. Estimated risk: {risk_level}%")

        fig, ax = plt.subplots()
        sns.barplot(x=["Low", "Medium", "High"], y=[30, 60, risk_level], color="gray")
        ax.bar(["Low", "Medium", "High"], [30, 60, risk_level], color=["green", "orange", "red"])
        st.pyplot(fig)

    st.write("\nThank you for playing! 🌟")

# Community Forum
elif page == "Community Forum":
    st.title("🌍 PCOS Community Forum")
    st.markdown("### Share experiences, tips, and support with others!")

    if "posts" not in st.session_state:
        st.session_state.posts = []
        st.session_state.upvotes = {}

    with st.form("new_post"):
        user_name = st.text_input("Your Name (or leave blank for anonymous):")
        user_message = st.text_area("Share your experience or ask a question:")
        submit_button = st.form_submit_button("Post")

        if submit_button and user_message:
            user_name = user_name if user_name else "Anonymous"
            post_id = len(st.session_state.posts)
            st.session_state.posts.append((post_id, user_name, user_message))
            st.session_state.upvotes[post_id] = 0
            st.success("✅ Post shared successfully!")

    st.markdown("---")

    if st.session_state.posts:
        for post_id, name, message in reversed(st.session_state.posts):
            st.markdown(f"**{name}:** {message}")
            if st.button(f"👍 {st.session_state.upvotes[post_id]}", key=f"upvote_{post_id}"):
                st.session_state.upvotes[post_id] += 1
            st.markdown("---")

# Lifestyle Quiz
elif page == "Lifestyle Quiz":
    st.title("🩺 PCOS Lifestyle Risk Assessment")
    questions = {
        "How often do you exercise?": {"Daily": 0, "3-5 times a week": 10, "1-2 times a week": 20, "Rarely": 30},
        "How would you rate your diet?": {"Excellent": 0, "Good": 10, "Average": 20, "Poor": 30},
        "Do you have irregular menstrual cycles?": {"Never": 0, "Occasionally": 10, "Often": 20, "Always": 30},
        "How stressed do you feel daily?": {"Not at all": 0, "Mildly": 10, "Moderately": 20, "Highly stressed": 30},
        "How many hours of sleep do you get per night?": {"More than 8": 0, "7-8 hours": 10, "5-6 hours": 20, "Less than 5": 30}
    }

    score = sum(o[st.radio(q, list(o.keys()), index=0)] for q, o in questions.items())
    st.subheader(f"📊 Your PCOS Risk Score: **{score}**")
