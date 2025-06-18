def recommend_inventory_action(current_inventory: dict, forecast: dict) -> dict:
    """
    Recommend inventory action: order difference if inventory < forecast, else hold.
    """
    recommendations = {}
    for sku, f in forecast.items():
        inv = current_inventory.get(sku, 0)
        if inv < f:
            recommendations[sku] = f - inv  # units to order
        else:
            recommendations[sku] = 0  # no order needed
    return recommendations
