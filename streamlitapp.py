import streamlit as st

def main():
    st.set_page_config(page_title='PCOS Prediction Dashboard', layout='wide')
    
    # Sidebar Navigation
    menu = ['Home', 'Games', 'Quiz', 'Health Condition', 'Symptoms', 'Causes', 'Preventive Measures']
    choice = st.sidebar.radio("Navigation", menu)
    
    # Page Layouts
    if choice == 'Home':
        st.title("Welcome to PCOS Prediction Dashboard")
        st.write("Explore various features related to PCOS awareness and prevention.")
    
    elif choice == 'Games':
        st.title("PCOS Awareness Games")
        st.write("Engaging and interactive games to learn more about PCOS.")
    
    elif choice == 'Quiz':
        st.title("PCOS Health Quiz")
        st.write("Take a quiz to assess your knowledge and awareness about PCOS.")
    
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
