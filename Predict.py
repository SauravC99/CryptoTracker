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

def predict(price):
    global new
    global old

    prices = [new, old]

    new = price
    old = prices[0]
    prices[0] = new
    prices[1] = old

    return prices

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
        value = predict(coin)
        if value[0] == value[1]:
            print("No change")
        elif value[0] > value[1]:
            print("More")
        else:
            print("less")
        time.sleep(3)

main()


