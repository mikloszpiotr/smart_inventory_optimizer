import streamlit as st
from utils.forecast_utils import forecast_demand
from utils.rl_utils import recommend_inventory_action

st.set_page_config(page_title="SmartInventory Optimizer", layout="wide")

st.title("📦 SmartInventory Optimizer")
st.markdown("Reduce stockouts and inventory costs using ML")

model_type = st.selectbox("Select ML Model", ["Time-Series Forecasting", "Reinforcement Learning"])

if model_type == "Time-Series Forecasting":
    st.subheader("🔮 Forecast Demand")
    forecast = forecast_demand()
    st.write(forecast)

elif model_type == "Reinforcement Learning":
    st.subheader("🧠 RL Inventory Optimization")
    recommendation = recommend_inventory_action()
    st.write(recommendation)
