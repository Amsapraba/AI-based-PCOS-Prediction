import streamlit as st
import random

def main():
    st.set_page_config(page_title='PCOS Prediction Dashboard', layout='wide')
    
    # Sidebar Navigation
    menu = ['Home', 'Games', 'Quiz', 'Health Condition', 'Symptoms', 'Causes', 'Preventive Measures']
    choice = st.sidebar.radio("Navigation", menu)
    
    # Page Layouts
    if choice == 'Home':
        st.title("Welcome to PCOS Prediction Dashboard")
        st.write("🌸 Empower yourself with knowledge about PCOS and take control of your health.")
        st.write("🔍 Explore insightful resources, interactive tools, and expert guidance.")
        st.write("🎯 Our mission is to spread awareness and provide actionable insights.")
        st.write("💡 Stay informed, stay healthy, and embrace a proactive approach to well-being.")
        st.write("🚀 Let's embark on this journey towards better health together!")
    
    elif choice == 'Games':
        st.title("Interactive Games")
        st.write("🎮 Engage with fun and educational games to test your knowledge about PCOS.")
        
        game_choice = st.selectbox("Choose a Game", ["MCQ Challenge", "Match the Symptoms", "Bubble Selection"])
        
        if game_choice == "MCQ Challenge":
            st.write("📝 Answer the multiple-choice questions correctly to earn points!")
            questions = [
                ("What hormone is typically elevated in PCOS?", ["Estrogen", "Progesterone", "Testosterone", "Insulin"], "Testosterone"),
                ("Which lifestyle change can help manage PCOS symptoms?", ["Eating more sugar", "Exercising regularly", "Skipping meals", "Sleeping less"], "Exercising regularly")
            ]
            score = 0
            for q, options, answer in questions:
                user_answer = st.radio(q, options)
                if user_answer == answer:
                    score += 1
                st.write(f"✅ Correct Answer: {answer}")
            if st.button("Submit Answers"):
                st.write(f"✅ Your Score: {score}/{len(questions)}")
        
        elif game_choice == "Match the Symptoms":
            st.write("🧩 Match the symptoms with the correct categories!")
            symptoms = {"Irregular periods": "Hormonal Imbalance", "Excessive hair growth": "Androgen Excess", "Weight gain": "Insulin Resistance", "Acne": "Hormonal Imbalance"}
            shuffled_keys = list(symptoms.keys())
            random.shuffle(shuffled_keys)
            score = 0
            for symptom in shuffled_keys:
                answer = st.selectbox(f"Match: {symptom}", ["Hormonal Imbalance", "Androgen Excess", "Insulin Resistance", "Other"])
                if answer == symptoms[symptom]:
                    score += 1
                st.write(f"✅ Correct Answer: {symptoms[symptom]}")
            if st.button("Submit Matches"):
                st.write(f"✅ Your Score: {score}/{len(symptoms)}")
        
        elif game_choice == "Bubble Selection":
            st.write("🎈 Select the correct bubbles related to PCOS management!")
            options = ["Healthy Diet", "Skipping Meals", "Regular Exercise", "Stress", "Adequate Sleep", "Insulin Resistance"]
            correct_answers = {"Healthy Diet", "Regular Exercise", "Adequate Sleep"}
            selected = st.multiselect("Choose the correct options:", options)
            if st.button("Submit Selections"):
                score = len(set(selected) & correct_answers)
                st.write(f"✅ Your Score: {score}/{len(correct_answers)}")
                st.write(f"✅ Correct Answers: {', '.join(correct_answers)}")
    
    elif choice == 'Quiz':
        st.title("PCOS Knowledge Quiz")
        st.write("🧠 Test your knowledge about PCOS and gain awareness.")
        questions = [
            ("What is a common symptom of PCOS?", ["High energy levels", "Irregular periods", "Low blood pressure", "Hair thinning"], "Irregular periods", "PCOS often causes irregular periods due to hormonal imbalances."),
            ("Which hormone is primarily responsible for insulin resistance in PCOS?", ["Cortisol", "Insulin", "Estrogen", "Androgens"], "Androgens", "Elevated androgens contribute to insulin resistance, a key feature of PCOS.")
        ]
        score = 0
        for q, options, answer, explanation in questions:
            user_answer = st.radio(q, options)
            if user_answer == answer:
                score += 1
            st.write(f"✅ Correct Answer: {answer}")
            st.write(f"ℹ️ Explanation: {explanation}")
        if st.button("Submit Quiz"):
            st.write(f"✅ Your Score: {score}/{len(questions)}")
    
if __name__ == "__main__":
    main()
