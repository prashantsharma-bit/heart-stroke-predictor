import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Page Config ----
st.set_page_config(page_title="Heart Stroke Predictor", layout="centered")

# ---- Load Model and Scaler ----
@st.cache_resource
def load_model():
    model = joblib.load('heart_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_model()

# ---- Title ----
st.title("❤️ Heart Stroke Risk Prediction Dashboard")
st.markdown("Enter your medical details below to check your risk of heart stroke.")

# ---- Input Fields (जैसे आपके model की features हैं) ----
st.subheader("Patient Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", options=["Male", "Female"])
    age = st.slider("Age", min_value=20, max_value=90, value=50)
    currentSmoker = st.radio("Current Smoker?", options=["No", "Yes"])
    cigsPerDay = st.slider("Cigarettes Per Day", min_value=0, max_value=70, value=0)
    BPMeds = st.radio("On Blood Pressure Medication?", options=["No", "Yes"])

with col2:
    prevalentStroke = st.radio("History of Stroke?", options=["No", "Yes"])
    prevalentHyp = st.radio("History of Hypertension?", options=["No", "Yes"])
    diabetes = st.radio("History of Diabetes?", options=["No", "Yes"])
    totChol = st.slider("Total Cholesterol (mg/dL)", min_value=100, max_value=600, value=240)
    sysBP = st.slider("Systolic Blood Pressure (mm Hg)", min_value=80, max_value=250, value=120)
    diaBP = st.slider("Diastolic Blood Pressure (mm Hg)", min_value=50, max_value=150, value=80)
    BMI = st.slider("BMI (Body Mass Index)", min_value=15.0, max_value=50.0, value=25.0, step=0.1)
    heartRate = st.slider("Heart Rate (bpm)", min_value=40, max_value=150, value=75)
    glucose = st.slider("Glucose Level (mg/dL)", min_value=40, max_value=400, value=80)

# ---- Convert Inputs to Numeric (जैसे model को चाहिए) ----
gender_encoded = 1 if gender == "Male" else 0
currentSmoker_enc = 1 if currentSmoker == "Yes" else 0
BPMeds_enc = 1 if BPMeds == "Yes" else 0
prevalentStroke_enc = 1 if prevalentStroke == "Yes" else 0
prevalentHyp_enc = 1 if prevalentHyp == "Yes" else 0
diabetes_enc = 1 if diabetes == "Yes" else 0

# ---- Predict Button ----
if st.button("🔍 Predict Heart Stroke Risk"):
    # 1. Build a DataFrame with the exact column names the model expects
    #    This ensures the feature order matches the training order exactly.
    input_df = pd.DataFrame([[
        gender_encoded,
        age,
        currentSmoker_enc,
        cigsPerDay,
        BPMeds_enc,
        prevalentStroke_enc,
        prevalentHyp_enc,
        diabetes_enc,
        totChol,
        sysBP,
        diaBP,
        BMI,
        heartRate,
        glucose
    ]], columns=[
        'Gender', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
        'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol',
        'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'
    ])

    # 2. Scale using the DataFrame (keeps column order consistent)
    input_scaled = scaler.transform(input_df)

    # 3. Prediction
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]  # Positive class (Stroke) की probability

    # 4. Result Display
    st.subheader("🩺 Prediction Result")
    
    if prediction[0] == 1:
        st.error(f"⚠️ **High Risk of Stroke Detected!** (Probability: {probability:.2%})")
        st.warning("Please consult a healthcare professional immediately.")
    else:
        st.success(f"✅ **Low Risk of Stroke.** (Probability: {probability:.2%})")
        st.info("Maintain a healthy lifestyle and keep monitoring your vitals.")

# ---- Optional: Debug Info (to check scaled input and model parameters) ----
with st.sidebar:
    st.header("📊 Model Insights")
    st.markdown("**Top Risk Factors (Based on Model):**")
    st.markdown("""
    - 🧓 **Age** (सबसे बड़ा कारक)
    - 💓 **Systolic BP** (उच्च रक्तचाप)
    - ⚖️ **BMI** (मोटापा)
    - 🚬 **Smoking Status**
    """)
    st.caption("This dashboard is for educational purposes only. Not a substitute for professional medical advice.")

    # ---- Debug section (expandable) ----
    with st.expander("🔍 Debug Info (for verification)", expanded=False):
        if 'input_scaled' in locals():
            st.write("**Scaled input (first 5 features):**", input_scaled[0][:5])
            st.write("**Model intercept:**", model.intercept_[0])
            st.write("**Model coefficients (first 5):**", model.coef_[0][:5])
            st.write("**Full scaled input:**", input_scaled)
        else:
            st.write("Run a prediction first to see debug info.")