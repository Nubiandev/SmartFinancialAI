import os
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("modeling/category_predictor.joblib")

# App title
st.title("📊 Smart Financial Insights AI")

# File upload or fallback
uploaded_file = st.file_uploader("📂 Upload your financial transactions CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    fallback_path = "sample_data/financial_transactions.csv"
    if os.path.exists(fallback_path):
        df = pd.read_csv(fallback_path)
        st.info("⚠️ No file uploaded — using sample data.")
    else:
        st.error("❌ No file uploaded and sample CSV not found.")
        st.stop()

# Show the data
st.subheader("📄 Transactions Preview")
st.dataframe(df)

# Predict categories if 'Description' column exists
if "Description" in df.columns:
    predictions = model.predict(df["Description"])
    df["Predicted Category"] = predictions

    st.subheader("🔍 Predicted Categories")
    st.dataframe(df[["Description", "Predicted Category"]])
else:
    st.warning("⚠️ 'Description' column not found in the uploaded data.")

# Optional: Keep your single input prediction too
st.subheader("📝 Try Single Transaction")
description = st.text_input("Enter a transaction description:")

if description:
    prediction = model.predict([description])[0]
    st.success(f"Predicted Category: {prediction}")
