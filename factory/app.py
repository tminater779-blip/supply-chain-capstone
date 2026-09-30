import streamlit as st
import joblib
import pandas as pd

# 1. Load the frozen model (the brain)
model = joblib.load('export_routing_engine.pkl')

# 2. Build the User Interface
st.title("📦 Supply Chain Routing Engine")
st.write("Enter the incoming order details to predict the required shipping route.")

# 3. Create input boxes for the user
quantity = st.number_input("Order Quantity", min_value=1, value=10)
unit_price = st.number_input("Unit Price", min_value=0.0, value=15.50)

# 4. Create the prediction button
if st.button("Predict Route"):
    input_data = pd.DataFrame([[quantity, unit_price]], columns=['Quantity', 'UnitPrice'])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("🌍 International Export (Customs Paperwork Required)")
    else:
        st.success("🚚 Standard Domestic Shipment")