import subprocess
import read_from_api as api

keep_asking = 1
av_crypto = ["BTC", "ETH"]
av_currency = ["EUR", "ARS", "USD"]
av_url = {"BTC": 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT',
          "ETH": 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey=9N3E66AEYSMKXXHT',
          "EUR": 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=9N3E66AEYSMKXXHT',
          "ARS": 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ARS&apikey=9N3E66AEYSMKXXHT',
          "USD": 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=USD&apikey=9N3E66AEYSMKXXHT'}

crypto, url = "", ''

# ask for crypto to query
while keep_asking:
    print("Seleccione la criptomoneda a consultar:")
    print("1.BTC")
    print("2.ETH")

    option = int(input())

    if option and option <= len(av_crypto):
        crypto = av_crypto[option - 1]
        keep_asking = 0
# end ask
print("\n..leyendo datos de la api..\n")
# leo la api para crypto
crypto_exchange_rate = api.get_exchange_rate(av_url[crypto])
ars = api.get_exchange_rate(av_url["ARS"])
euro = api.get_exchange_rate(av_url["EUR"])

subprocess.run(["../calc", crypto, crypto_exchange_rate, ars, euro])



