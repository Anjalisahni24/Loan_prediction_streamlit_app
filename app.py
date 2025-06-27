import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('loan_model.pkl')

st.title("Loan Approval Prediction System")

# User inputs
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
self_employed = st.selectbox("Are you self-employed?", ["No", "Yes"])
income_annum = st.number_input("Annual Income (₹)", min_value=0)
loan_amount = st.number_input("Loan Amount (₹)", min_value=0)
loan_term = st.number_input("Loan Term (in months)", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)
residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0)
bank_asset_value = st.number_input("Bank Balance / Asset Value (₹)", min_value=0)

# Prepare input for model
input_data = np.array([[
    no_of_dependents,
    1 if self_employed == "Yes" else 0,
    income_annum,
    loan_amount,
    loan_term,
    cibil_score,
    residential_assets_value,
    commercial_assets_value,
    luxury_assets_value,
    bank_asset_value
]])

# Prediction logic with input validation
if st.button("Predict Loan Approval"):
    if income_annum < 50000:
        st.warning("⚠️ Income is too low to be eligible for a loan.")
    elif loan_amount > income_annum * 10:
        st.warning("⚠️ Loan amount is too high compared to annual income.")
    elif cibil_score < 600:
        st.warning("⚠️ Low CIBIL score may lead to rejection.")
    else:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.success(f"✅ Loan Approved!\n\nConfidence: {probability:.2%}")
        else:
            st.error(f"❌ Loan Rejected.\n\nConfidence: {probability:.2%}")
