import streamlit as st
import requests
import os

# For local development: http://127.0.0.1:8000
# For production: use your deployed backend URL
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.title("Insurance Charges Prediction")

st.subheader("Enter your details to predict insurance charges")

#input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", options=[0.0, 1.0], format_func=lambda x: "Male" if x == 0.0 else "Female")
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, value=2)
smoker = st.selectbox("Smoker", options=[0.0, 1.0], format_func=lambda x: "No" if x == 0.0 else "Yes")
region = st.number_input("Region (0-3)", min_value=0, max_value=3, value=2)

if st.button("Predict Charges"):
    input_data = {
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region,
    }

    try:
        response = requests.post(API_URL, json=input_data, timeout=10)
        response.raise_for_status()
        result = response.json()
        st.success(f"Predicted Insurance Charges: Rs{result['predicted_charges']:.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")