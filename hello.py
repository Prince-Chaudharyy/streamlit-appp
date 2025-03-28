import streamlit as st
import joblib  # or import pickle if you used pickle
import pandas as pd

# Load the trained model
try:
    model = joblib.load("model.pkl")  # Update with your actual model file path
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'model.pkl' is in the correct directory.")
    model = None

# Streamlit UI
st.title("Order-to-Delivery Time Prediction")
st.write("Enter order details to predict the expected delivery time.")

# User inputs
product_category = st.selectbox("Product Category", ["Electronics", "Clothing", "Home", "Books"])
customer_location = st.text_input("Customer Location (City/State)")
shipping_method = st.selectbox("Shipping Method", ["Standard", "Express", "Same-day"])
order_weight = st.number_input("Order Weight (kg)", min_value=0.1, step=0.1)

# Predict button
if st.button("Predict Delivery Time"):
    if model is not None:
        # Create a DataFrame with user input
        input_data = pd.DataFrame({
            "product_category": [product_category],
            "customer_location": [customer_location],
            "shipping_method": [shipping_method],
            "order_weight": [order_weight]
        })
        
        try:
            # Make prediction
            prediction = model.predict(input_data)[0]
            # Display result
            st.success(f"Estimated Delivery Time: {prediction:.2f} days")
        except Exception as e:
            st.error(f"An error occurred while making the prediction: {e}")
    else:
        st.error("Prediction cannot be made because the model is not loaded.")

