import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title='PCOS Prediction Dashboard', layout='wide')
    
    # Sidebar Navigation
    menu = ['Home', 'Symptoms', 'Causes', 'Preventive Measures', 'Health Condition', 'Quiz', 'Games', 'Upload & View Data']
    choice = st.sidebar.radio("Navigation", menu)
    
    if choice == 'Home':
        st.title("AI-based Early Detection and Prediction of Poly Cystic Ovary Syndrome (PCOS)")
        st.write("### Amsapraba A P (Team Leader), Akshaya A, Kanaga Durga E, Srimathi P, Sam V George (MENTOR)")
        st.write("#### St. Joseph’s College of Engineering, Chennai.")
        st.write("**Team Code: S179**")
        st.subheader("Welcome to the PCOS Prediction Dashboard")
        st.write("🔍 Explore insights and tools for early detection and management of PCOS.")
        st.write("📊 Utilize AI-driven predictions for proactive healthcare decisions.")
        st.write("💡 Stay informed, stay healthy!")
    
    elif choice == 'Symptoms':
        st.subheader("⚠️ Symptoms of PCOS")
        st.write("- 📌 Irregular menstrual cycles")
        st.write("- 📌 Excessive hair growth (hirsutism)")
        st.write("- 📌 Acne and oily skin")
        st.write("- 📌 Weight gain and difficulty losing weight")
        st.write("- 📌 Thinning hair or hair loss on the scalp")
    
    elif choice == 'Causes':
        st.subheader("🧐 Causes of PCOS")
        st.write("- 🔬 Insulin resistance leading to increased blood sugar levels.")
        st.write("- 🏋️‍♀️ Excess androgen production causing hormonal imbalances.")
        st.write("- 🧬 Genetic factors increasing susceptibility to PCOS.")
        st.write("- 🔥 Chronic inflammation linked to insulin resistance and metabolic issues.")
    
    elif choice == 'Preventive Measures':
        st.subheader("🛡️ Preventive Health Measures for PCOS")
        st.write("- 🥗 Maintain a healthy diet rich in whole foods and low in processed sugars.")
        st.write("- 🏃‍♀️ Engage in regular physical activity to improve insulin sensitivity.")
        st.write("- 🧘‍♀️ Manage stress through mindfulness, yoga, and relaxation techniques.")
        st.write("- 😴 Ensure adequate sleep to maintain hormonal balance.")
        st.write("- 🩺 Consult healthcare professionals for early detection and proactive management.")
    
    elif choice == 'Health Condition':
        st.subheader("🩺 Check Your Health Condition")
        st.write("Assess your risk and take steps towards a healthier lifestyle.")
    
    elif choice == 'Quiz':
        st.subheader("🧠 PCOS Knowledge Quiz")
        st.write("Test your understanding of PCOS and related health aspects.")
    
    elif choice == 'Games':
        st.subheader("🎮 Fun and Interactive Games")
        st.write("Learn more about PCOS in an engaging way!")
    
    elif choice == 'Upload & View Data':
        st.subheader("📂 Upload and View PCOS Dataset")
        uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("### Uploaded Data")
            st.dataframe(df)
    
if __name__ == "__main__":
    main()
