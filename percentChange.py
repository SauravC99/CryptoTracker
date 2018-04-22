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

a = getPrice()
new = a["BTC"]
old = new

def percentChange(price):
    global new
    global old

    old = new
    new = price

    change = ((new - old) / old) * 100
    print(new)
    print(old)
    return change


def main():
    while True:
        all_coins = getPrice()  # get dictionary from APIs
        #Replace with coin from graphics
        coin = all_coins["BTC"]#get the coin
        value = percentChange(coin)
        print(value)
        time.sleep(300)

main()
