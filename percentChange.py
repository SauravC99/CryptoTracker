from API import *
import time

a = getPrice()
new = a["BTC"]
old = new

def percentChange(price):
    global new
    global old

    #Set old to last new price, update new price
    old = new
    new = price

    #Find percent change
    change = ((new - old) / old) * 100
    return change

def alert(percent):
    pass

def main():
    while True:
        #Get dictionary from API
        all_coins = getPrice()
        #Replace with coin from graphics
        coin = all_coins["BTC"]
        value = percentChange(coin)
        print(value)
        #Loop every 5 minutes because that's when API updates
        time.sleep(300)

main()
