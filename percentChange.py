from __future__ import print_function
from telesign.messaging import MessagingClient
from historicalPrice import *
from currentPrice import *
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
    #Telesign API Code
    customer_id = "BA0A590D-1B52-49E7-8C20-C082D986B309"
    api_key = "5TIV0NDzn2afvWmWscxjPidghGWEY+55hZYXSig4dgML6uUZ67pWvcGa9JtswmS1hea8GMP7HQmBHnB1gwIasg=="

    phone_number = getPhoneNumber()
    message = "{0} has gone up {1} percent in the last 5 minutes!".format(getCoin(), percent)
    message_type = "ARN"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)

def getThreshold():
    #Get from graphics float
    pass

def getPhoneNumber():
    #Get number from graphics int
    pass

def getCoin():
    #Get from graphics String
    pass

def main():
    while True:
        #Get dictionary from API
        all_coins = getPrice()
        #Replace with coin from graphics
        coin = all_coins[getCoin()]

        #Get percent change
        value = percentChange(coin)
        #Send SMS alert if it is greater than user's threshold
        if value >= getThreshold():
            alert(value)

        print(value)
        #Loop every 5 minutes because that's when API updates
        time.sleep(300)

main()
