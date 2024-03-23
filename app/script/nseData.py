from nselib import capital_market

def companiesStockPriceHistory(symbol="TCS", from_date="01-01-2023", to_date="04-03-2024"):
    data = capital_market.price_volume_and_deliverable_position_data(
        symbol=symbol, from_date=from_date, to_date=to_date)
    print(data)
    return data
