import pandas as pd

def forecast_demand(data: pd.DataFrame, window: int = 3) -> dict:
    """
    Compute moving average forecast for the next period per SKU.
    """
    data['Sales'] = pd.to_numeric(data['Sales'])
    data = data.sort_values(['SKU', 'Date'])
    data['Forecast'] = data.groupby('SKU')['Sales'].transform(lambda x: x.rolling(window, min_periods=1).mean())
    last_forecast = data.groupby('SKU')['Forecast'].last()
    return last_forecast.to_dict()
