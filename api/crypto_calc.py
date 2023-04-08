import request
import subprocess

keep_asking = 1
av_crypto = ["BTC", "ETH"]
av_currency = ["EUR", "ARS", "USD"]
crypto, currency = "", ""

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


