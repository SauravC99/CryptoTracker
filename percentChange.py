'''
coninually check the prices in a loop
compare to see if up or down
see how much it goes up
if growth slows, see how much it does
when growth is <1% say it might fall now
same for loss
'''
from API import *
import time

new = 0
old = 0

def first(price):
    global new
    global old

    prices = [new, old]

    new = price
    old = prices[0]
    prices[0] = new
    prices[1] = old
    return prices

def percentChange(price):

    prices = first(price)
    prices = first(price)

    change = ((prices[0] - prices[1]) / prices[1]) * 100
    print(prices)
    return change

def getDict():
    return getPrice()

def getCoin():
    #Get coin from Graphics
    pass


def main():
    while True:
        all_coins = getDict()  # get dictionary from APIs
        #Replace with coin from graphics
        coin = all_coins["BTC"]#get the coin
        value = percentChange(coin)
        print(value)
        time.sleep(300)

main()
