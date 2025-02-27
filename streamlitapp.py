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
        st.title("PCOS Awareness Games")
        game_choice = st.radio("Choose a game:", ["PCOS Trivia", "Puzzle Challenge", "Find the Myth"])
        
        if game_choice == "PCOS Trivia":
            st.subheader("PCOS Trivia - Answer the MCQs")
            questions = {
                "What is a common symptom of PCOS?": ["Irregular periods", "Low blood pressure", "Increased vision", "Stronger bones"],
                "Which hormone is often elevated in PCOS?": ["Insulin", "Testosterone", "Estrogen", "Melatonin"],
                "What lifestyle change can help manage PCOS?": ["Exercise", "Skipping meals", "Ignoring symptoms", "Sleeping less"]
            }
            score = 0
            for q, options in questions.items():
                answer = st.radio(q, options)
                if answer == options[0]:
                    score += 1
            if st.button("Submit Answers"):
                if score >= 2:
                    st.success(f"Great job! You scored {score}/3 and won 10 points!")
                else:
                    st.error(f"Keep learning! You scored {score}/3. Try again!")
        
        elif game_choice == "Puzzle Challenge":
            st.subheader("Match the Correct Terms")
            pairs = {"PCOS": "Hormonal disorder", "Insulin Resistance": "Can lead to diabetes", "Exercise": "Helps in PCOS management"}
            score = 0
            for key in pairs:
                match = st.selectbox(f"{key} is related to:", ["Hormonal disorder", "Can lead to diabetes", "Helps in PCOS management", "Unrelated"])
                if match == pairs[key]:
                    score += 1
            if st.button("Check Answers"):
                if score >= 2:
                    st.success(f"Awesome! You scored {score}/3 and won 10 points!")
                else:
                    st.error(f"Try again! You scored {score}/3.")
        
        elif game_choice == "Find the Myth":
            st.subheader("Spot the Myth - Select the incorrect statement")
            myths = {
                "PCOS is curable": False,
                "Only overweight women get PCOS": False,
                "PCOS can affect fertility": True,
                "PCOS is always caused by genetics": False
            }
            score = 0
            for statement, truth in myths.items():
                selection = st.radio(f"{statement}", ["True", "False"])
                if (selection == "False" and not truth) or (selection == "True" and truth):
                    score += 1
            if st.button("Submit"):
                if score >= 3:
                    st.success(f"You're a myth buster! You scored {score}/4 and won 10 points!")
                else:
                    st.error(f"Almost there! You scored {score}/4. Try again!")
    
    elif choice == 'Quiz':
        st.title("PCOS Health Quiz")
        st.write("Take a quiz to assess your knowledge and awareness about PCOS.")
        
        quiz_questions = {
            "What is PCOS caused by?": ["Hormonal imbalance", "Bacterial infection", "Vitamin deficiency", "Excess hydration"],
            "Which symptom is NOT commonly linked to PCOS?": ["Frequent colds", "Irregular periods", "Weight gain", "Acne"],
            "What is a recommended dietary approach for managing PCOS?": ["Low sugar, high fiber", "High sugar, low fiber", "Only liquid diet", "No carbohydrates"],
            "Which organ is primarily affected by PCOS?": ["Ovaries", "Liver", "Heart", "Lungs"]
        }
        
        quiz_score = 0
        for q, options in quiz_questions.items():
            answer = st.radio(q, options)
            if answer == options[0]:
                quiz_score += 1
        
        if st.button("Submit Quiz"):
            if quiz_score >= 3:
                st.success(f"Excellent! You scored {quiz_score}/4. Keep up the good work!")
            else:
                st.warning(f"You scored {quiz_score}/4. Keep learning and try again!")
    
    elif choice == 'Health Condition':
        st.title("Check Your Health Condition")
        st.write("Understand your health status based on different parameters.")
    
    elif choice == 'Symptoms':
        st.title("PCOS Symptoms")
        st.write("Learn about the common symptoms of PCOS and their impact.")
    
    elif choice == 'Causes':
        st.title("Causes of PCOS")
        st.write("Explore the potential causes and risk factors of PCOS.")
    
    elif choice == 'Preventive Measures':
        st.title("Preventive Measures")
        st.write("Find out how to reduce the risk of PCOS through lifestyle changes.")
    
if __name__ == "__main__":
    main()
