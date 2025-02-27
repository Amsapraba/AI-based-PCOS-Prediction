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
page = st.sidebar.radio("Go to", ["Home", "PCOS Prediction Game", "Community Forum", "Lifestyle Quiz", "Healthy Recipes"])

# Home Section
if page == "Home":
    st.title("🏥 PCOS Prediction Dashboard")
    st.write("Welcome to the PCOS Prediction App! Navigate through the sidebar to explore features.")

# Community Forum
elif page == "Community Forum":
    st.title("🌍 PCOS Community Forum")
    st.markdown("### Share your feelings, symptoms, and feedback!")

    if "posts" not in st.session_state:
        st.session_state.posts = []
        st.session_state.upvotes = {}

    with st.form("new_post"):
        user_name = st.text_input("Your Name (or leave blank for anonymous):")
        user_feelings = st.text_area("How do you feel today?")
        user_symptoms = st.text_area("Describe any symptoms you're experiencing:")
        user_feedback = st.text_area("Any feedback or suggestions for the community?")
        submit_button = st.form_submit_button("Post")

        if submit_button and (user_feelings or user_symptoms or user_feedback):
            user_name = user_name if user_name else "Anonymous"
            post_id = len(st.session_state.posts)
            post_content = f"**Feelings:** {user_feelings}\n**Symptoms:** {user_symptoms}\n**Feedback:** {user_feedback}"
            st.session_state.posts.append((post_id, user_name, post_content))
            st.session_state.upvotes[post_id] = 0
            st.success("✅ Post shared successfully!")

    st.markdown("---")

    if st.session_state.posts:
        for post_id, name, message in reversed(st.session_state.posts):
            st.markdown(f"**{name}:**\n{message}")
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

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Lifestyle Risk Meter"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "blue"}}
    ))
    st.plotly_chart(fig)

# Healthy Recipes
elif page == "Healthy Recipes":
    st.title("🍏 Healthy Recipes for PCOS")
    st.write("Explore nutritious and easy-to-make recipes that can help manage PCOS symptoms.")

    recipes = {
        "Avocado & Egg Toast": "Toast whole-grain bread, top with mashed avocado and a poached egg, season with salt & pepper.",
        "Berry Smoothie": "Blend mixed berries, Greek yogurt, chia seeds, and almond milk for a refreshing smoothie.",
        "Quinoa Salad": "Mix cooked quinoa, cherry tomatoes, cucumber, feta cheese, and a lemon-olive oil dressing.",
        "Oatmeal with Nuts & Seeds": "Cook oats with almond milk, top with walnuts, flaxseeds, and a drizzle of honey.",
        "Grilled Salmon with Veggies": "Season salmon with herbs, grill with bell peppers and zucchini, serve with brown rice."
    }

    for recipe, instructions in recipes.items():
        st.subheader(recipe)
        st.write(instructions)
