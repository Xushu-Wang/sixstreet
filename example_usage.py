from stock_api import StockAPI

# Initialize with your Alpha Vantage API key
api = StockAPI("YOUR_API_KEY")

# Lookup data for a specific date
data = api.lookup("IBM", "2023-05-15")
print(f"IBM on 2023-05-15: {data}")

# Get minimum low price over last 10 days
min_price = api.min("IBM", 10)
print(f"Minimum low price (last 10 days): {min_price}")

# Get maximum high price over last 10 days
max_price = api.max("IBM", 10)
print(f"Maximum high price (last 10 days): {max_price}")