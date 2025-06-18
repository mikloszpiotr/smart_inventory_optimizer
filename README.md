# Smart Inventory Optimizer

Smart Inventory Optimizer is a Streamlit-based web application that enables supply chain and inventory professionals to make smarter, data-driven inventory decisions using machine learning and time-series forecasting.

## Features

- **Easy Data Upload:** Upload your inventory and sales data in CSV format.
- **Multiple Forecasting Models:** Choose from four popular time-series forecasting models:
    - **Naive (Moving Average):** Simple rolling average, quick baseline for short-term trends.
    - **Holt-Winters (Exponential Smoothing):** Captures trend and seasonality, ideal for cyclical demand.
    - **ARIMA:** Statistical model for short- and long-term demand patterns with auto-regressive components.
    - **Prophet:** Robust forecasting from Facebook, handles holidays and multiple seasonality, good for business data.
- **KPI Dashboard:** Instantly visualize critical supply chain KPIs, including:
    - Stockout Rate
    - Service Level
    - Inventory Turnover
    - Average Inventory
    - Overstock Rate
- **Inventory Policy Simulation:** Example of a rule-based reorder policy to demonstrate optimization logic.
- **Sample Data Included:** Try the app immediately with sample data provided.

## Business Value

- **Lower Costs:** More accurate forecasting helps minimize excess inventory, freeing up capital.
- **Improve Service Levels:** Reduce out-of-stocks and avoid missed sales.
- **Make Decisions Faster:** Compare model performance and choose the best approach for your business context.
- **Adapt to Change:** Test the impact of new sales patterns or supply chain disruptions before they happen.

## Why These Models?

- **Naive Model:** Provides a fast benchmark; easy to interpret.
- **Holt-Winters:** Great for demand with clear seasonal patterns (e.g., weekly, monthly).
- **ARIMA:** Widely used for time-series, effective for auto-correlated sales.
- **Prophet:** Handles real-world business data well, with holidays and trend shifts.

## How to Use

1. **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```
2. **Start the App**
    ```bash
    streamlit run app.py
    ```
3. **Upload Data**
    - Use the sidebar to upload your CSV.
    - Select forecasting model.
    - Explore dashboard for KPIs and forecasts.

## Folder Structure

- `app.py` – Main Streamlit app
- `utils/` – Data processing and ML modules
- `data/` – Sample data for testing
- `requirements.txt` – All dependencies

---

*Accelerate your supply chain transformation with Smart Inventory Optimizer—bring advanced analytics to your inventory decisions!*
