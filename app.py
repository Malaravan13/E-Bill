import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('trained_model.sav', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("Electricity Bill Predictor ⚡")

st.write("Enter the number of units consumed to predict the electricity bill amount.")

# Input
Units = st.number_input("Units Consumed:", min_value=0, max_value=10000, value=100)

features = np.array([[Units]])

# Prediction button
if st.button("Predict Bill"):
    prediction = model.predict(features)
    st.success(f"Estimated Bill Amount: ₹{prediction[0]:,.2f}")
