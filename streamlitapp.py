import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

st.set_page_config(page_title="Health Tracking Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "Non-Invasive Assessment", "Invasive Assessment", "Symptom-Based AI Prediction", "Health Quiz", "Community Support"])

if page == "Home":
    st.title("Welcome to the Health Tracking Game!")
    st.write("Log your health, interact with the community, and test your knowledge!")
    
elif page == "Non-Invasive Assessment":
    st.title("Non-Invasive Health Assessment")
    st.write("Enter your non-invasive health details to analyze your PCOS risk.")
    
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    weight_gain = st.radio("Have you experienced weight gain?", ["Yes", "No"])
    hair_loss = st.radio("Are you experiencing hair loss?", ["Yes", "No"])
    fast_food = st.radio("Do you consume fast food frequently?", ["Yes", "No"])
    pimples = st.radio("Do you have frequent pimples?", ["Yes", "No"])
    exercise = st.radio("Do you exercise regularly?", ["Yes", "No"])
    
    if st.button("Analyze Risk"):
        responses = [weight_gain, hair_loss, fast_food, pimples, exercise]
        risk_score = responses.count("Yes") / len(responses) * 100
        
        labels = ["Healthy", "At Risk"]
        sizes = [100 - risk_score, risk_score]
        colors = ["#76c7c0", "#ff6f61"]
        
        st.subheader("Your PCOS Risk Levels")
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        st.pyplot(fig)
        
        st.success("Assessment completed! Consult a doctor for more insights.")
    
    st.subheader("Ideal Health Distribution for Women")
    fig, ax = plt.subplots()
    ax.pie([90, 10], labels=["Healthy", "At Risk"], autopct='%1.1f%%', colors=["#76c7c0", "#ff6f61"], startangle=90)
    st.pyplot(fig)
    
elif page == "Invasive Assessment":
    st.title("Invasive Health Assessment")
    st.write("Enter your invasive test results to analyze your PCOS risk.")
    
    uploaded_file = st.file_uploader("Upload your lab results (CSV)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        invasive_features = df.columns.difference(["Age", "BMI", "Weight Gain", "Hair Loss", "Fast Food", "Pimples", "Regular Exercise"])
        selected_features = st.multiselect("Select parameters to include:", invasive_features)
        
        if selected_features:
            values = {feature: st.number_input(f"{feature}", min_value=0.0) for feature in selected_features}
            
            if st.button("Analyze Risk"):
                risk_score = np.mean(list(values.values()))
                labels = ["Healthy", "At Risk"]
                sizes = [100 - risk_score, risk_score]
                colors = ["#76c7c0", "#ff6f61"]
                
                st.subheader("Your PCOS Risk Levels")
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
                st.pyplot(fig)
                
                st.success("Assessment completed! Consult a doctor for more insights.")
    
    st.subheader("Ideal Health Distribution for Women")
    fig, ax = plt.subplots()
    ax.pie([90, 10], labels=["Healthy", "At Risk"], autopct='%1.1f%%', colors=["#76c7c0", "#ff6f61"], startangle=90)
    st.pyplot(fig)
    
# The rest of the pages remain unchanged.
elif page == "Symptom-Based AI Prediction":
    st.title("AI Symptom Prediction")
    st.write("Enter your symptoms, and the AI will suggest possible conditions.")
    symptom_input = st.text_area("Describe your symptoms (e.g., headache, fever, fatigue)")
    if st.button("Predict Condition"):
        example_conditions = {"headache fever fatigue": "Possible flu or viral infection"}
        st.subheader("Prediction Result")
        st.write(f"The AI suggests: **{example_conditions.get(symptom_input, 'Consult a doctor')}**")
        st.success("This is a basic prediction. Consult a doctor for accurate medical advice.")
    
elif page == "Health Quiz":
    st.title("Health Knowledge Quiz")
    st.write("Test your knowledge about health and wellness!")
    questions = {"What is a normal resting heart rate?": ["60-100 BPM", "30-50 BPM", "120-150 BPM"]}
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
