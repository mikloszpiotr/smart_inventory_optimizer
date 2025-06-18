from prophet import Prophet

def prophet_forecast(data):
    results = {}
    for sku in data['SKU'].unique():
        sub = data[data['SKU'] == sku].sort_values('Date')
        dfp = sub.rename(columns={'Date': 'ds', 'Sales': 'y'})[['ds', 'y']]
        model = Prophet(daily_seasonality=True, yearly_seasonality=False)
        model.fit(dfp)
        future = model.make_future_dataframe(periods=1, freq='D', include_history=True)
        forecast = model.predict(future)
        yhat = forecast.iloc[-1]['yhat']
        results[sku] = yhat
    return results
