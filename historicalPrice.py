# #This is the API Python file
#
#
# # # # # # LIMITS FOR COINMARKET CAP API # # # # #
#
# #   1. Limit requests to no more than 10 per minute #
#
# #   2. Endpoints update every 5 minutes             #
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

import requests
import datetime


def currency(limit, symbol):
    # displays the prices for a month every half day
    #Returns 60-62 data points
    if limit == "month":
        time = 730

        url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}' \
                .format(symbol, "USD", time, 1)
        page = requests.get(url)
        _dict = {}
        df = page.json()['Data']
        for i in range(0,len(df),12):
            dict_ = df[i]
            time = dict_["time"]
            _dict[time] = df[i]["close"]
        return _dict

    # displays the prices for a week every hour
    #Returns 168 data points
    elif limit == "week":
        time = 168
        url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(symbol, "USD", time, 1)
        page = requests.get(url)
        _dict = {}
        df = page.json()['Data']
        range_= len(df)
        for i in range(0, len(df), 1):
            dict_ = df[i]
            time = dict_["time"]
            _dict[time] = df[i]["close"]
        return _dict
    # displays the prices for a day every 20 minutes
    #Returns 72 data points
    elif limit == "day":
        time = 1500

        url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(symbol, "USD", time, 1)
        page = requests.get(url)
        _dict = {}
        df = page.json()['Data']
        for i in range(0, len(df), 20):
            dict_ = df[i]
            time = dict_["time"]
            _dict[time] = i
        return _dict

#asks for user input for currency and time frame
def main():
    curr_input = input("What currency do you want? (symbol; ex. (BTC)")
    time_frame = input("What time frame? (ex. month, day, week)")
    print(currency(time_frame, curr_input))


