import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.forecast_utils import moving_average_forecast, holt_winters_forecast, arima_forecast
from utils.prophet_utils import prophet_forecast
from utils.rl_utils import recommend_inventory_action

st.set_page_config(page_title="SmartInventory Optimizer", layout="wide")
st.title("📦 SmartInventory Optimizer")
st.markdown("Analyze and optimize inventory using ML models.")

# Load data
data = pd.read_csv("data/sample_inventory_data.csv", parse_dates=['Date'])

if st.checkbox("Show raw data"):
    st.dataframe(data)

model_type = st.selectbox(
    "Select Forecasting Model",
    ["Moving Average", "Holt-Winters", "ARIMA", "Prophet"]
)

if model_type == "Moving Average":
    forecast = moving_average_forecast(data)
elif model_type == "Holt-Winters":
    forecast = holt_winters_forecast(data)
elif model_type == "ARIMA":
    forecast = arima_forecast(data)
elif model_type == "Prophet":
    forecast = prophet_forecast(data)
else:
    st.warning("Model not implemented")
    forecast = {}

current_inventory = data.sort_values('Date').groupby('SKU')['Inventory'].last().to_dict()
summary_df = pd.DataFrame({
    'SKU': list(forecast.keys()),
    'Forecast Next Period': list(forecast.values()),
    'Current Inventory': [current_inventory.get(sku, 0) for sku in forecast.keys()]
})
st.subheader("Forecast vs Current Inventory")
st.table(summary_df)

st.subheader("Inventory Recommendations")
recs = recommend_inventory_action(current_inventory, forecast)
st.json(recs)

st.subheader("Demand Forecast Chart")
fig, ax = plt.subplots()
ax.bar(summary_df['SKU'], summary_df['Forecast Next Period'])
ax.set_xlabel("SKU")
ax.set_ylabel("Forecasted Units")
st.pyplot(fig)
