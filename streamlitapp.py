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

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_level,
            title={"text": "PCOS Risk Meter"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 40], "color": "green"},
                    {"range": [40, 70], "color": "yellow"},
                    {"range": [70, 100], "color": "red"}
                ],
                "bar": {"color": "blue"}
            }
        ))
        st.plotly_chart(fig)

    st.write("\nThank you for playing! 🌟")
