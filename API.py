from requests.auth import HTTPBasicAuth
import requests
from bs4 import BeautifulSoup

class PineappleAPI():
    
    BASE_URL = "https://orderbookz.com/bluelagoon/api"

    def __init__(self):

        # Api keys
        self.api_key = 'VJEOL'
        self.timeout = 300
        self.headers = {"api-key" : self.api_key}

    def balance(self):

        # API path of candlesticks
        path = "%s/balance" % self.BASE_URL

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.get(url, headers=self.headers, timeout=self.timeout, verify=True).json()

    def orderbook(self):

        # API path of candlesticks
        path = "%s/orderbook" % self.BASE_URL

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.get(url, headers=self.headers, timeout=self.timeout, verify=True).json()

    def orders_active(self):

        # API path of candlesticks
        path = "%s/orders/active" % self.BASE_URL

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.get(url, headers=self.headers, timeout=self.timeout, verify=True).json()

    def trades(self): 

        # API path of candlesticks
        path = "%s/trades" % self.BASE_URL

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.get(url, headers=self.headers, timeout=self.timeout, verify=True).json()

    def submit(self, price, quantity, side, tif):

        # API path of candlesticks
        path = "%s/submit" % self.BASE_URL

        # Get parameters
        params = {"p": price, "q": quantity, "d": side, "tif": tif}

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.post(url, headers=self.headers, timeout=self.timeout, verify=True, json=params).json()

    def cancel(self, orderid):

        # API path of candlesticks
        path = "%s/cancel" % self.BASE_URL

        # Get parameters
        params = {"id": orderid}

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.put(url, headers=self.headers, timeout=self.timeout, verify=True, json=params).json()

    def cancel_all(self):

        # API path of candlesticks
        path = "%s/cancel/all" % self.BASE_URL

        # Construct URL
        url = "%s" % (path)

        # Request data
        return requests.put(url, headers=self.headers, timeout=self.timeout, verify=True).json()
    
#pa = PinneappleAPI()

#output = pa.balance() # 'money' gives the amount of money, (min=-100.000). 'stock' gives the amount of stocks (max=30)
#output = pa.orderbook() # Gives the orderbook, 'buy' and 'sell'
#output = pa.orders_active() # Gives the open orders in a list
#output = pa.trades() # Gives all past trades
#output = pa.submit(10, 15, 'buy', 'GTC') # Put in buy or sell order
#orderid = 'BLGX000001002'
#output = pa.cancel(orderid) # Cancel order by id
#output = pa.cancel_all() # Cancel all
#print(output)