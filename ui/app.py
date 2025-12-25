# ui/app.py
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

# ---------- Page Header ----------
st.title("🩺💼 Health Insurance Premium Predictor")
st.caption("🤖 AI-powered premium estimation • Fast • Reliable")

st.divider()

# ---------- Input Fields ----------
age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1)
dependants = st.number_input("👨‍👩‍👧 Number of Dependants", min_value=0, max_value=10, step=1)
income = st.number_input("💰 Annual Income (Lakhs)", min_value=0, max_value=200, step=1)
genetical_risk = st.number_input("🧬 Hereditary Risk Index", min_value=0, max_value=5, step=1)

insurance_plan = st.selectbox("📄 Insurance Plan", ["Bronze", "Silver", "Gold"])
gender = st.selectbox("🚻 Gender", ["Male", "Female"])
marital_status = st.selectbox("💍 Marital Status", ["Married", "Unmarried"])
employment_status = st.selectbox("🏢 Employment Status", ["Salaried", "Self-Employed"])
bmi = st.selectbox("⚖️ BMI Category", ["Normal", "Overweight", "Obesity", "Underweight"])
smoking = st.selectbox("🚬 Smoking Status", ["No Smoking", "Occasional", "Regular"])
region = st.selectbox("📍 Region", ["Northwest", "Southeast", "Southwest"])
medical_history = st.selectbox(
    "🩻 Pre-Existing Conditions",
    [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Heart disease",
        "Diabetes & High blood pressure",
        "Diabetes & Heart disease",
        "Thyroid",
    ],
)

st.divider()

# ---------- Prediction ----------
if st.button("🔍 Predict Premium"):
    payload = {
        "age": age,
        "dependants": dependants,
        "income": income,
        "genetical_risk": genetical_risk,
        "insurance_plan": insurance_plan,
        "gender": gender,
        "marital_status": marital_status,
        "employment_status": employment_status,
        "bmi": bmi,
        "smoking": smoking,
        "region": region,
        "medical_history": medical_history,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        if response.status_code == 200:
            result = response.json()
            st.success(f"💸 Estimated Insurance Premium: ₹ {result['predicted_premium']:,}")
        else:
            st.error("❌ API error. Please try again later.")

    except requests.exceptions.RequestException:
        st.error("🚫 Unable to connect to API. Make sure the server is running.")
