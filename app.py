import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.forecast_utils import forecast_demand
from utils.prophet_utils import prophet_forecast
from utils.rl_utils import recommend_inventory_action

st.set_page_config(page_title="SmartInventory Optimizer", layout="wide")
st.title("📦 SmartInventory Optimizer")
st.markdown("Analyze and optimize inventory using ML models.")

# Load data
data = pd.read_csv("data/sample_inventory_data.csv", parse_dates=['Date'])

if st.checkbox("Show raw data"):
    st.dataframe(data)

# Model selection
model_type = st.selectbox("Select Forecasting Model", ["Moving Average", "Prophet"])

# Forecast based on selection
if model_type == "Moving Average":
    forecast = forecast_demand(data)
else:
    forecast = prophet_forecast(data)

# Current inventory
current_inventory = data.sort_values('Date').groupby('SKU')['Inventory'].last().to_dict()

# Display summary
summary_df = pd.DataFrame({
    'SKU': list(forecast.keys()),
    'Forecast Next Period': list(forecast.values()),
    'Current Inventory': list(current_inventory.values())
})
st.subheader("Forecast vs Current Inventory")
st.table(summary_df)

# Recommendations
st.subheader("Inventory Recommendations")
recs = recommend_inventory_action(current_inventory, forecast)
st.json(recs)

# Forecast chart
st.subheader("Demand Forecast Chart")
fig, ax = plt.subplots()
ax.bar(summary_df['SKU'], summary_df['Forecast Next Period'])
ax.set_xlabel("SKU")
ax.set_ylabel("Forecasted Units")
st.pyplot(fig)
