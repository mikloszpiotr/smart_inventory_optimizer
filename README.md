# Smart Inventory Optimizer

**Smart Inventory Optimizer** is a Streamlit-based application for supply chain analytics and inventory optimization.  
This project demonstrates how modern machine learning and time series forecasting can drive better business decisions in inventory management.

---

## 🚀 Project Overview

This app helps supply chain professionals:
- Predict product demand using multiple advanced forecasting models.
- Evaluate and recommend optimal inventory levels for each SKU.
- Visualize critical supply chain KPIs for smarter business decisions.

---

## 🔍 Business Problems Addressed

- **How can we accurately forecast future product demand?**
- **How much inventory should we hold for each SKU to avoid stockouts and minimize overstock?**
- **Which SKUs are most at risk for inventory shortages or surplus?**
- **How do different forecasting models impact our service levels and cost?**

---

## 🧠 Machine Learning & Forecasting Models Used

1. **Moving Average**
   - Simple baseline; helps track short-term demand trends.
2. **Holt-Winters (Exponential Smoothing)**
   - Captures seasonality and trends; ideal for cyclical sales.
3. **ARIMA**
   - Advanced statistical model for time series with auto-regressive and moving average components.
4. **Prophet**
   - State-of-the-art model from Meta, robust to seasonality and holiday effects.

---

## 📊 Key Features

- **Multiple Forecasting Models:** Easily compare the performance of different models on your own data.
- **Automated Inventory Recommendations:** Get recommended reorder quantities for every SKU based on forecasted demand, current inventory, and a safety buffer.
- **Critical Inventory KPIs:** Current Inventory, Forecasted Demand and more.
- **Flexible Data Input:** Upload your own CSV with sales, inventory, and SKU data.
- **Sample Data Included:** Try the app instantly without setup.

---

## 💡 Business Impact

- **Reduce Stockouts:** Minimize lost sales and customer dissatisfaction by forecasting demand more accurately.
- **Cut Inventory Costs:** Avoid costly overstock and optimize working capital.
- **Data-Driven Decision Making:** Enable faster, more confident decisions at every stage of the supply chain.
- **Benchmark Model Performance:** Select the best forecasting approach for your business scenario.

---

## 🏗️ Project Structure

- `app.py` — Streamlit web application
- `utils/forecast_utils.py` — Classical forecasting models
- `utils/prophet_utils.py` — Prophet model
- `utils/rl_utils.py` — Inventory recommendation logic
- `data/sample_inventory_data.csv` — Example dataset
- `requirements.txt` — Dependencies

---

## ⚙️ How to Use

1. **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the app:**  
    ```bash
    streamlit run app.py
    ```
3. **Upload your data or use sample data**
4. **Select a forecasting model and review dashboard**
5. **Use automated recommendations for smarter replenishment**

---

## 📈 Example KPIs Visualized

- **Forecasted demand per SKU**
- **Current inventory per SKU**
- **Recommended reorder quantity**
- **Service level, stockout risk, turnover**

---

*Built for modern supply chain analytics. Accelerate your inventory optimization with ML-driven insights!*
