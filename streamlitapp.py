import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

st.set_page_config(page_title="PCOS ML Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "What is PCOS?", "PCOS Dataset", "Data Visualization", "PCOS Prediction"])

if page == "Home":
    st.title("Welcome to Our PCOS ML Game!")
    st.write("Explore PCOS in a fun and interactive way!")
    
elif page == "What is PCOS?":
    st.title("What is PCOS?")
    st.write("Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder in women. It can lead to irregular periods, excessive androgen levels, and ovarian cysts. Early diagnosis and management are crucial.")
    
    st.subheader("Symptoms:")
    st.markdown("- Irregular periods")
    st.markdown("- Excessive hair growth (hirsutism)")
    st.markdown("- Acne and oily skin")
    st.markdown("- Weight gain and difficulty losing weight")
    st.markdown("- Thinning hair or hair loss")
    st.markdown("- Fertility issues")
    
    st.subheader("Causes:")
    st.markdown("- Genetic factors")
    st.markdown("- Insulin resistance")
    st.markdown("- Excess androgen production")
    st.markdown("- Lifestyle and environmental factors")
    
    st.subheader("Effects:")
    st.markdown("- Increased risk of type 2 diabetes")
    st.markdown("- High blood pressure and heart disease")
    st.markdown("- Depression and anxiety")
    st.markdown("- Sleep apnea")
    st.markdown("- Infertility or complications in pregnancy")
    
    st.subheader("Precautions & Management:")
    st.markdown("- Maintaining a healthy diet and regular exercise")
    st.markdown("- Managing stress levels")
    st.markdown("- Consulting a healthcare provider for medical treatments")
    st.markdown("- Monitoring weight and hormone levels")

elif page == "PCOS Dataset":
    st.title("PCOS Dataset")
    st.write("Upload the dataset to view the complete data.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

elif page == "Data Visualization":
    st.title("Data Visualization")
    st.write("Explore key insights from the dataset through visualizations.")
    
    uploaded_file = st.file_uploader("Upload CSV file for visualization", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Clean BMI column
        df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')  # Convert invalid values to NaN
        df = df.dropna(subset=['BMI'])  # Drop rows where BMI is NaN

        st.subheader("Distribution of PCOS Cases")
        fig, ax = plt.subplots()
        sns.countplot(x='PCOS (Y/N)', data=df, ax=ax)
        st.pyplot(fig)
        
        st.subheader("BMI Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['BMI'], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
        
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10,6))
        
        # Select only numeric columns for correlation
        numeric_df = df.select_dtypes(include=['number']).dropna()
        sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

elif page == "PCOS Prediction":
    st.title("PCOS Prediction Model")
    st.write("Upload the dataset to train and test a machine learning model.")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Ensure numeric data
        df = df.select_dtypes(include=['number']).dropna()
        
        # Define features and target
        X = df.drop(columns=['PCOS (Y/N)'])
        y = df['PCOS (Y/N)']
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Standardizing data
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        # Train Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        st.subheader("Model Performance")
        st.write(f"Accuracy: {accuracy * 100:.2f}%")
        st.text("Classification Report:")
        report = classification_report(y_test, y_pred)
        st.text(report)
        
        st.subheader("Understanding the Metrics")
        st.markdown("**Precision:** Measures how many predicted positive cases were actually correct.")
        st.markdown("- Class 0 (No PCOS): High precision means most predicted 'No PCOS' cases were correct.")
        st.markdown("- Class 1 (PCOS): Lower precision means some predicted 'PCOS' cases were incorrect.")
        
        st.markdown("**Recall:** Measures how many actual positive cases were correctly predicted.")
        st.markdown("- Class 0 (No PCOS): High recall means most 'No PCOS' cases were detected correctly.")
        st.markdown("- Class 1 (PCOS): Lower recall means some PCOS cases were missed.")
        
        st.markdown("**F1-Score:** Balances precision and recall, higher is better.")
        
        st.markdown("**Support:** Number of actual samples per class.")
        
        st.subheader("Possible Improvements")
        st.markdown("- Balance the dataset using resampling techniques.")
        st.markdown("- Try different models like SVM, XGBoost, or Neural Networks.")
        st.markdown("- Improve feature selection for better accuracy.")
        st.markdown("- Use hyperparameter tuning to optimize the model.")
