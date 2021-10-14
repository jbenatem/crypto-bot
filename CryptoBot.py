import requests
from Entities.CryptoCurrency import CryptoCurrency

def GetCurrentCryptoQuote(id):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + str(id)
    authToken = 'INSERT YOUR AUTH TOKEN'
    request = requests.get(url, headers = {"X-CMC_PRO_API_KEY": authToken})
    if (request.status_code == 200):
        quote = round(request.json()["data"]["1"]["quote"]["USD"]["price"],2)
        return quote
    else:
        raise Exception("Get current crypto currency quote request failed")

def ConvertBitcoinToDollars(totalBitcoins, quote):
    amount = round(totalBitcoins * quote,2)
    return amount

def main():
    # Obtener total de dólares disponibles en billetera digital
    initialWallet = 100.00
    # Obtener total de bitcoins disponibles en billetera digital
    initialBitcoinAmount = 0.00180819
    # Obtener precio de Bitcoin
    quote = GetCurrentCryptoQuote(1)
    print('--------------------------PRECIO BITCOIN--------------------------')
    print(quote)
    print('------------------------------------------------------------------')
    # Convertir valor de bitcoins en dolares
    amount = ConvertBitcoinToDollars(initialBitcoinAmount, quote)
    print('--------------------------PRECIO BITCOIN--------------------------')
    print('USD ' + str(amount))
    print('------------------------------------------------------------------')

if __name__ == "__main__":
    print('CryptoBot started!!')
    while True:
        main()