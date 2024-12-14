import requests

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/last_prices')
async def get_last_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum,tether,binancecoin,solana,xrp,cardano,avalanche-2&vs_currencies=usd'
    res = requests.get(url)
    data = res.json()

    prices = {
        'Ethereum': data['ethereum']['usd'],
        'Tether': data['tether']['usd'],
        'Binance Coin': data['binancecoin']['usd'],
        'Solana': data['solana']['usd'],
        'Cardano': data['cardano']['usd'],
        'Avalanche': data['avalanche-2']['usd'],
    }
    return prices


@app.get('/market_caps')
async def get_market_caps():
    return {'message': 'Hello World'}

