import pandas as pd
from prophet import Prophet

def prophet_forecast(data: pd.DataFrame) -> dict:
    """
    Use Facebook Prophet to forecast the next day's demand per SKU.
    """
    forecasts = {}
    for sku, grp in data.groupby('SKU'):
        df = grp[['Date', 'Sales']].rename(columns={'Date': 'ds', 'Sales': 'y'})
        m = Prophet(daily_seasonality=True, weekly_seasonality=True)
        m.fit(df)
        future = m.make_future_dataframe(periods=1, freq='D')
        pred = m.predict(future)
        next_y = pred.iloc[-1]['yhat']
        forecasts[sku] = max(0, int(round(next_y)))
    return forecasts
