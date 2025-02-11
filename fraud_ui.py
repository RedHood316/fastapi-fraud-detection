import streamlit as st
import requests
import json

# FastAPI Endpoint
API_URL = "http://127.0.0.1:8000/predict"  # Change if deployed online

# Streamlit App UI
st.title("💳 Credit Card Fraud Detection")
st.write("🔍 Enter transaction details to check if it's fraudulent.")

# User input fields
features = []
for i in range(30):  # Expecting 30 features
    value = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(value)

# Predict button
if st.button("🔮 Predict Fraud"):
    data = {"features": features}
    
    # Call FastAPI
    try:
        response = requests.post(API_URL, json=data)
        result = response.json()

        # Display prediction
        if response.status_code == 200:
            if result["fraud_prediction"] == 1:
                st.error("🚨 Fraudulent Transaction Detected! 🚨")
            else:
                st.success("✅ Transaction is Safe!")
        else:
            st.warning(f"⚠️ Error: {result}")
    except Exception as e:
        st.error(f"❌ API Error: {e}")
