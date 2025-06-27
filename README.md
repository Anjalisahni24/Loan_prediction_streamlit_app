# 🏦 Loan Approval Prediction App

A machine learning-powered web app built with [Streamlit](https://streamlit.io/) that predicts whether a user's loan application will be approved based on financial and personal details.

## 🚀 Live Demo
🔗 [Click here to use the app](https://loanpredictionappapp-s3cyhmzoqomhcgofyyf6sy.streamlit.app/)  

---

## 📦 Features

- Predicts loan approval using a trained ML model (`loan_model.pkl`)
- Uses inputs like income, assets, CIBIL score, loan amount, and more
- Shows model confidence (probability)
- Input validation and warnings for unrealistic data

---

## 🧠 Model Info

- Trained using `GridSearchCV` with the best estimator
- Input features:
  - `no_of_dependents`
  - `self_employed`
  - `income_annum`
  - `loan_amount`
  - `loan_term`
  - `cibil_score`
  - `residential_assets_value`
  - `commercial_assets_value`
  - `luxury_assets_value`
  - `bank_asset_value`

---

## 📁 Project Structure

─ app.py # Streamlit app
─ loan_model.pkl # Trained machine learning model
─ requirements.txt # Python dependencies
─ README.md # Project description


---

## 🧪 Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Anjalisahni24/loan-approval-app.git
   cd loan-prediction_steamlit_app
   '''
2. Install dependencies:
   '''bash
   pip install -r requirements.txt
'''
4. Run the app:
'''bash
streamlit run app.py
'''
