import requests

api_response = requests.get('https://data-api.binance.vision/api/v3/avgPrice?symbol=BTCUSDT')
bitcoin_price = float(api_response.json()['price'])

print(f'The average price of Bitcoin for the past 5 minutes is {bitcoin_price:.2f}.')