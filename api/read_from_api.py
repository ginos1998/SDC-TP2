import requests


def get_exchange_rate(url):
    req = requests.get(url)
    data = req.json()
    crypto_exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return crypto_exchange_rate


