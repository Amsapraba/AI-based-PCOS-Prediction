import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

st.set_page_config(page_title="PCOS ML Game", page_icon="✨")

page = st.sidebar.radio("Navigation", ["Home", "What is PCOS?", "PCOS Dataset", "Data Visualization", "PCOS Prediction"])

if page == "Home":
    st.title("Welcome to Our PCOS ML Game!")
    st.write("Explore PCOS in a fun and interactive way!")
    
elif page == "What is PCOS?":
    st.title("What is PCOS?")
    st.write("Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder in women.")
    
elif page == "PCOS Dataset":
    st.title("PCOS Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

elif page == "Data Visualization":
    st.title("Data Visualization")
    uploaded_file = st.file_uploader("Upload CSV file for visualization", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Distribution of PCOS Cases")
        fig, ax = plt.subplots()
        sns.countplot(x='PCOS (Y/N)', data=df, ax=ax)
        st.pyplot(fig)

elif page == "PCOS Prediction":
    st.title("PCOS Prediction Model")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = df.select_dtypes(include=['number']).dropna()
        X = df.drop(columns=['PCOS (Y/N)'])
        y = df['PCOS (Y/N)']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"Accuracy: {accuracy * 100:.2f}%")

# AI-Based Symptom Prediction
scaler = MinMaxScaler()
def normalize_data(data):
    return scaler.fit_transform(data)

def prepare_lstm_data(data, time_steps=10):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:i+time_steps])
        y.append(data[i+time_steps])
    return np.array(X), np.array(y)

def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def predict(model, data):
    predictions = model.predict(data)
    return scaler.inverse_transform(predictions)

def suggest_challenges(predictions):
    if predictions[-1] > 0.7:
        return "Try a stress-relief activity today!"
    elif predictions[-1] < 0.3:
        return "Great progress! Keep up your healthy habits."
    else:
        return "Maintain consistency with your routine."

def calculate_rewards(predictions):
    if predictions[-1] < 0.3:
        return "You've earned 50 reward points!"
    elif predictions[-1] > 0.7:
        return "You've earned 20 points for tracking your symptoms."
    else:
        return "Consistent effort! 30 points added to your score."

data = pd.read_csv('pcos_data.csv')
data_normalized = normalize_data(data[['symptom_severity']])
X, y = prepare_lstm_data(data_normalized)
model = build_lstm_model((X.shape[1], X.shape[2]))
model.fit(X, y, epochs=20, batch_size=16, verbose=1)
future_prediction = predict(model, X[-1].reshape(1, X.shape[1], X.shape[2]))
challenge = suggest_challenges(future_prediction)
reward = calculate_rewards(future_prediction)

print("Predicted Symptom Severity:", future_prediction[-1])
print("AI Challenge Suggestion:", challenge)
print("Reward Earned:", reward)
