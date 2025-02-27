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
    
    elif choice == 'Quiz':
        st.title("PCOS Knowledge Quiz")
        st.write("🧠 Test your knowledge about PCOS and gain awareness.")
        questions = [
            ("What is a common symptom of PCOS?", ["High energy levels", "Irregular periods", "Low blood pressure", "Hair thinning"], "Irregular periods"),
            ("Which hormone is primarily responsible for insulin resistance in PCOS?", ["Cortisol", "Insulin", "Estrogen", "Androgens"], "Androgens")
        ]
        score = 0
        for q, options, answer in questions:
            user_answer = st.radio(q, options)
            if user_answer == answer:
                score += 1
        if st.button("Submit Quiz"):
            st.write(f"✅ Your Score: {score}/{len(questions)}")
    
    elif choice == 'Health Condition':
        st.title("Monitor Your Health Condition")
        st.write("📊 Track these parameters to monitor your health:")
        st.markdown("- 📅 **Menstrual Cycle**: Keep a log of your periods to identify irregularities.")
        st.markdown("- ⚖️ **Weight & BMI**: Maintain a healthy weight to regulate hormones.")
        st.markdown("- 🍽️ **Diet & Sugar Levels**: Monitor blood sugar levels to prevent insulin resistance.")
        st.markdown("- 🩸 **Hormone Levels**: Get tested for testosterone, insulin, and other key hormones.")
        st.markdown("- 🏃 **Exercise Routine**: Stay physically active to improve metabolism and hormonal balance.")
    
    elif choice == 'Symptoms':
        st.title("PCOS Symptoms")
        st.write("⚠️ Common symptoms of PCOS include:")
        st.markdown("- ❌ Irregular or absent menstrual cycles")
        st.markdown("- 🌱 Excessive hair growth (hirsutism)")
        st.markdown("- 🎭 Acne and oily skin")
        st.markdown("- ⚖️ Unexplained weight gain")
        st.markdown("- 💤 Fatigue and sleep disturbances")
        st.markdown("- 🧑‍⚕️ Difficulty in conceiving (infertility)")
        st.markdown("- 📉 Thinning hair or hair loss on the scalp")
    
    elif choice == 'Causes':
        st.title("Causes of PCOS")
        st.write("🔍 Potential causes and risk factors of PCOS:")
        st.markdown("- ⚙️ **Hormonal Imbalance**: Increased androgens leading to irregular ovulation")
        st.markdown("- 🧬 **Genetics**: Family history of PCOS or hormonal disorders")
        st.markdown("- 🍩 **Insulin Resistance**: High insulin levels contribute to weight gain and hormonal disruptions")
        st.markdown("- 🍕 **Unhealthy Diet & Lifestyle**: Poor nutrition, lack of exercise, and obesity increase risks")
        st.markdown("- 💊 **Inflammation**: Chronic low-grade inflammation can exacerbate PCOS symptoms")
    
    elif choice == 'Preventive Measures':
        st.title("Preventive Measures")
        st.write("✅ Ways to reduce the risk and manage PCOS effectively:")
        st.markdown("- 🥗 **Healthy Diet**: Eat a balanced diet rich in fiber, protein, and healthy fats")
        st.markdown("- 🏃 **Regular Exercise**: Engage in physical activities like walking, yoga, or strength training")
        st.markdown("- 🛌 **Adequate Sleep**: Maintain a consistent sleep schedule to regulate hormones")
        st.markdown("- 🏥 **Regular Checkups**: Consult a doctor for hormone tests and health assessments")
        st.markdown("- 🚫 **Reduce Stress**: Practice mindfulness, meditation, and relaxation techniques")
        st.markdown("- 🍬 **Limit Sugar Intake**: Control blood sugar levels to manage insulin resistance")
    
if __name__ == "__main__":
    main()
