'''
simple program to access specific "live" stock market data from yahoo finance page and extract stock market "ticker" data

url format = "https://uk.finance.yahoo.com/quote/<ticker-code>&quot;
e.g https://uk.finance.yahoo.com/quote/MSFT/

plan
----
* import yfinance
* make request to yahoo finance with qualifier in url, e.g. MSFT
* check return code from request
* if success, parse data "fetch what we need"
* display following data
* repeat until exit
'''

# declare libaries
#from bs4 import BeautifulSoup
import yfinance as yf

#import requests

# declare data structures

# declare functions
def make_request(ticker):

    ticker = yf.Ticker(ticker)
    info = ticker.info
   
    if info is None or info.get("regularMarketPrice") is None:
        print("No market data")
        result = -1
    else:
        result = ticker
    #end if

    return result

#end def


def parse_info(ticker):

    print(ticker.history())

#end def


def print_stock_data():

    pass

#end def


# main starts here
exit = False

while not exit:

    code = input("\nEnter Stock Ticker Code (or X to Exit)..> ").upper()
    if code == "X":
        print("Bye!")
        exit = True
    else:

        result = make_request(code)
        if result == -1:
            print("\nRequest Failed\n")
            continue
        else:
            parse_info(result)
        #end if

    #end if

#end while