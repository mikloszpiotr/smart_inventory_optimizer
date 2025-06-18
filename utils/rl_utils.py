def recommend_inventory_action(current_inventory, forecast, buffer=5):
    recommendations = {}
    for sku in forecast.keys():
        needed = max(int(round(forecast[sku] + buffer - current_inventory.get(sku, 0))), 0)
        recommendations[sku] = needed
    return recommendations
