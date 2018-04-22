from __future__ import print_function
from telesign.messaging import MessagingClient
from CryptoTracker.historicalPrice import *
from CryptoTracker.currentPrice import *
import time

a = getPrice()
new = a["BTC"]
old = new

perCheck = 0

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

    global perCheck
    if perCheck > 0:
        message = "{0} has gone up {1} percent in the last 5 minutes!".format(getCoin(), percent)
    if perCheck < 0:
        message = "{0} has gone down {1} percent in the last 5 minutes!".format(getCoin(), percent)
    message_type = "ARN"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)

def getDayThreshold():
    file = open("dayPercentage.txt", "r")
    dayPercentage = file.read()
    file.close()
    return float(dayPercentage)

def getMinuteThreshold():
    file = open("minutePercentage.txt", "r")
    minutePercentage = file.read()
    file.close()
    return float(minutePercentage)

def getPhoneNumber():
    file = open("phone.txt", "r")
    number = file.read()
    file.close()
    return number

def getChangeMonth(coin):
    values = currency("month", coin)
    #Get a list of the values of the dictionary
    values = list(values.values())
    change = ((values[-1] - values[0]) / values[0]) * 100
    return change

def getChangeWeek(coin):
    values = currency("week", coin)
    #Get a list of the values of the dictionary
    values = list(values.values())
    change = ((values[-1] - values[0]) / values[0]) * 100
    return change

def getChangeDay(coin):
    values = currency("day", coin)
    #Get a list of the values of the dictionary
    values = list(values.values())
    change = ((values[-1] - values[0]) / values[0]) * 100
    return change

def main():
    while True:
        #Get dictionary from API
        all_coins = getPrice()
        #Replace with coin from graphics
        coin = all_coins["BTC"]

        #Get percent change
        value = percentChange(coin)
        #Send SMS alert if it is greater than user's threshold
        global perCheck
        perCheck = value
        if value < 0:
            value = value * -1
        if value >= getDayThreshold() or value >= getMinuteThreshold():
            alert(value)

        print(value)
        #Loop every 5 minutes because that's when API updates
        time.sleep(300)

#main()

