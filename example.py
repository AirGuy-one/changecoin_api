import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum,tether,binancecoin,solana,xrp,cardano,avalanche-2&vs_currencies=usd'

response = requests.get(url)
data = response.json()

print(f"Ethereum price: ${data['ethereum']['usd']}")
print(f"Tether price: ${data['tether']['usd']}")
print(f"Binance Coin price: ${data['binancecoin']['usd']}")
print(f"Solana price: ${data['solana']['usd']}")
print(f"Cardano price: ${data['cardano']['usd']}")
print(f"Avalanche price: ${data['avalanche-2']['usd']}")
