# api/test_model.py
from api.inference import predict_premium

sample_input = {
    "age": 30,
    "dependants": 2,
    "income": 12,
    "genetical_risk": 1,
    "insurance_plan": "Gold",
    "gender": "Male",
    "marital_status": "Married",
    "employment_status": "Salaried",
    "bmi": "Overweight",
    "smoking": "No Smoking",
    "region": "Southwest",
    "medical_history": "Diabetes"
}

print(predict_premium(sample_input))
