import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('loan_model.pkl')

st.title("Loan Approval Prediction")

# Create input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Process input
if st.button("Predict"):
    input_data = np.array([
        # Make sure order matches training
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        2 if property_area == "Urban" else (1 if property_area == "Semiurban" else 0)
    ]).reshape(1, -1)

    prediction = model.predict(input_data)
    st.success("Loan Approved" if prediction[0] == 1 else "Loan Rejected")
