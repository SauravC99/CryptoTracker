# # # # # LIMITS FOR COINMARKET CAP API # # # # #

#   1. Limit requests to no more than 10 per minute #

#   2. Endpoints update every 5 minutes             #

# # # # # # # # # # # # # # # # # # # # # # # # # # #
#import needed modules

import coinmarketcap

def getPrice():

    market = coinmarketcap.Market()

    #this is a dictionary of the top 5 cryptocurrency
    #to index a specific item:
    #print(coin_dictionary["name of crypto"][0]["name of what you want to print, i.e "id"]
    coin_dictionary = {"BTC" : market.ticker("Bitcoin"),
    "ETH" : market.ticker("Ethereum"),
    "XRP" : market.ticker("Ripple"),
    "BCH" : market.ticker("bitcoin-cash"),
    "EOS" : market.ticker("EOS")}

    price_and_value_dictionary = {}
    # this loops through each key in the dictionary and retrieves the symbol and price
    # for each currency.
    for key in coin_dictionary:

        symbol = coin_dictionary[key][0]["symbol"]
        price = coin_dictionary[key][0]["price_usd"]
        price_and_value_dictionary[symbol] = float(price)
    return(price_and_value_dictionary)
getPrice()