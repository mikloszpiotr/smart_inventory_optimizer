# 📦 SmartInventory Optimizer

## 🎯 Purpose
Optimize inventory levels and avoid stockouts using ML-driven demand forecasts.

## ML Models
- **Moving Average:** Rolling-window average of past sales.
- **Prophet:** Facebook Prophet for advanced trend and seasonality capture.

## How It Works
1. Load sales & inventory data.
2. Choose forecasting model (Moving Average or Prophet).
3. View forecast vs. current inventory.
4. Get reorder recommendations using a simple RL-based rule.

## Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
```
