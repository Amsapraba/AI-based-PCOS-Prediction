import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Page Configuration
st.set_page_config(page_title="PCOS Prediction", layout="wide")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Home", "Upload Data", "Visualize Data", "Predict PCOS"])

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_").str.lower()
    return df

if menu == "Home":
    st.title("Welcome to AI-Based PCOS Risk Prediction")
    st.write("This application helps in predicting the risk of PCOS based on crucial health parameters. Upload your dataset to get started!")

elif menu == "Upload Data":
    st.title("Upload PCOS Dataset")
    uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df = clean_column_names(df)
        st.write("Dataset Loaded Successfully!")
        st.dataframe(df.head())
        df.to_csv("pcos_data.csv", index=False)  # Save uploaded data

elif menu == "Visualize Data":
    st.title("PCOS Data Visualization")
    
    # Load dataset
    try:
        df = pd.read_csv("pcos_data.csv")
        df = clean_column_names(df)
        st.write("Showing crucial PCOS-related features:")
        features = ["age_yrs", "bmi", "cycle_length_days", "fsh_miu_ml", "lh_miu_ml", "amh_ng_ml",
                    "tsh_miu_l", "follicle_no_l", "follicle_no_r", "avg_f_size_l_mm", "avg_f_size_r_mm",
                    "endometrium_mm", "weight_gain_y_n", "hair_growth_y_n", "skin_darkening_y_n",
                    "hair_loss_y_n", "pimples_y_n", "fast_food_y_n", "reg_exercise_y_n"]
        df = df[features + ["pcos_y_n"]]
        
        # Barplot
        st.subheader("Bar Plot of PCOS Cases")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x="pcos_y_n", palette="coolwarm", ax=ax)
        st.pyplot(fig)
        
        # Histograms
        st.subheader("Histogram of Selected Features")
        selected_feature = st.selectbox("Select a feature", features)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_feature], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
        
        # Pie Chart
        st.subheader("Pie Chart for Lifestyle Factors")
        pie_feature = st.selectbox("Select a feature for pie chart", ["weight_gain_y_n", "hair_growth_y_n", "skin_darkening_y_n", "hair_loss_y_n", "pimples_y_n"])
        fig, ax = plt.subplots()
        df[pie_feature].value_counts().plot.pie(autopct="%.1f%%", ax=ax)
        st.pyplot(fig)
    
    except FileNotFoundError:
        st.warning("Please upload the dataset first!")

elif menu == "Predict PCOS":
    st.title("PCOS Prediction")
    
    # Load and train model
    try:
        df = pd.read_csv("pcos_data.csv")
        df = clean_column_names(df)
        features = ["age_yrs", "bmi", "cycle_length_days", "fsh_miu_ml", "lh_miu_ml", "amh_ng_ml",
                    "tsh_miu_l", "follicle_no_l", "follicle_no_r", "avg_f_size_l_mm", "avg_f_size_r_mm",
                    "endometrium_mm", "weight_gain_y_n", "hair_growth_y_n", "skin_darkening_y_n",
                    "hair_loss_y_n", "pimples_y_n", "fast_food_y_n", "reg_exercise_y_n"]
        
        X = df[features]
        y = df["pcos_y_n"]
        
        # Data Preprocessing
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Train Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, "pcos_model.pkl")
        joblib.dump(scaler, "scaler.pkl")
        
        st.success("Model Trained Successfully!")
    
    except FileNotFoundError:
        st.warning("Please upload the dataset first!")
    
    # Prediction Inputs
    st.subheader("Enter Details for Prediction")
    user_input = [st.number_input(f"{feature}") for feature in features]
    
    if st.button("Predict PCOS"):
        try:
            model = joblib.load("pcos_model.pkl")
            scaler = joblib.load("scaler.pkl")
            user_input_scaled = scaler.transform([user_input])
            prediction = model.predict(user_input_scaled)
            result = "PCOS Detected" if prediction[0] == 1 else "No PCOS"
            st.success(f"Prediction Result: {result}")
        except:
            st.error("Model not found. Please train the model first!")
