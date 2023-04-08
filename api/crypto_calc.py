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

crypto, currency, url = "", "", ''

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

keep_asking = 1

# ask for currency to convert
while keep_asking:
    print("Seleccione la moneda de conversión:")
    print("1.EUR")
    print("2.ARS")
    print("3.USD")

    option = int(input())

    if option and option <= len(av_currency):
        currency = av_currency[option - 1]
        keep_asking = 0

# end ask

print("Convertir {c} --> {m}".format(c=crypto, m=currency))

# leo la api para crypto
crypto_exchange_rate = api.get_exchange_rate(av_url[crypto])
# leo de la api para moneda
currency_exchange_rate = api.get_exchange_rate(av_url[currency])

# muestro el resultado
result = "\nPrecio criptomoneda: {str1}\nPrecio moneda: {str2}".format(str1=crypto_exchange_rate,
                                                                       str2=currency_exchange_rate)
print(result)

subprocess.run(["./calc", crypto_exchange_rate, currency_exchange_rate])



