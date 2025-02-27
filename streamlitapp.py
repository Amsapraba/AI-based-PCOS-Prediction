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
    
    elif choice == 'Symptoms':
        st.title("⚠️ Symptoms of PCOS")
        st.write("- 📌 **Irregular menstrual cycles**")
        st.write("- 📌 **Excessive hair growth (hirsutism)**")
        st.write("- 📌 **Acne and oily skin**")
        st.write("- 📌 **Weight gain and difficulty losing weight**")
        st.write("- 📌 **Thinning hair or hair loss on the scalp**")
    
    elif choice == 'Causes':
        st.title("🧐 Causes of PCOS")
        st.write("- 🔬 **Insulin resistance** - Reduces the body's ability to use insulin effectively.")
        st.write("- 🏋️‍♀️ **Excess androgen production** - Leads to symptoms like excessive hair growth and acne.")
        st.write("- 🧬 **Genetic factors** - A family history of PCOS may increase the likelihood of developing the condition.")
        st.write("- 🔥 **Chronic inflammation** - Linked to higher androgen levels and insulin resistance.")
    
    elif choice == 'Preventive Measures':
        st.title("🛡️ Preventive Health Measures for PCOS")
        st.write("- 🥗 **Maintain a healthy diet** - Consume whole foods, fiber-rich meals, and avoid processed sugars.")
        st.write("- 🏃‍♀️ **Engage in regular physical activity** - Exercise helps improve insulin sensitivity and manage symptoms.")
        st.write("- 🧘‍♀️ **Manage stress effectively** - Mindfulness, yoga, and relaxation techniques can help balance hormones.")
        st.write("- 😴 **Ensure adequate sleep** - Maintain a consistent sleep schedule to regulate hormonal balance.")
        st.write("- 🩺 **Consult a healthcare professional** - Early detection and proactive management can prevent complications.")
    
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
            user_answers = {}
            for i, (q, options, answer) in enumerate(questions):
                user_answers[i] = st.radio(q, options, key=f"mcq_{i}")
            if st.button("Submit Answers"):
                for i, (_, _, answer) in enumerate(questions):
                    st.write(f"✅ Correct Answer: {answer}")
                    if user_answers[i] == answer:
                        score += 1
                st.write(f"✅ Your Score: {score}/{len(questions)}")
    
if __name__ == "__main__":
    main()
