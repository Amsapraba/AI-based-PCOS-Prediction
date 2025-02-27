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
