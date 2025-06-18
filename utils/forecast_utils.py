import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

def moving_average_forecast(data, window=3):
    results = {}
    for sku in data['SKU'].unique():
        sub = data[data['SKU'] == sku].sort_values('Date')
        ma = sub['Sales'].rolling(window=window, min_periods=1).mean().iloc[-1]
        results[sku] = ma
    return results

def holt_winters_forecast(data, seasonal_periods=7):
    results = {}
    for sku in data['SKU'].unique():
        sub = data[data['SKU'] == sku].sort_values('Date')
        if len(sub) >= seasonal_periods:
            model = ExponentialSmoothing(sub['Sales'], seasonal='add', seasonal_periods=seasonal_periods)
            fit = model.fit()
            forecast = fit.forecast(1).iloc[0]
        else:
            forecast = sub['Sales'].mean()
        results[sku] = forecast
    return results

def arima_forecast(data, order=(2,1,2)):
    results = {}
    for sku in data['SKU'].unique():
        sub = data[data['SKU'] == sku].sort_values('Date')
        if len(sub) > sum(order):
            model = ARIMA(sub['Sales'], order=order)
            fit = model.fit()
            forecast = fit.forecast(1).iloc[0]
        else:
            forecast = sub['Sales'].mean()
        results[sku] = forecast
    return results
