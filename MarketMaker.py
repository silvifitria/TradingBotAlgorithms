import API
import time
import requests
from bs4 import BeautifulSoup

api = API.PineappleAPI()

#{'error': 'Too Many Requests', 'message': 'Easy there tiger'}

class MarketMaker():

    def __init__(self):

        self.min_spread = 0.9
        self.max_loss = 1
        self.amount = 15

    def trade(self):

        cancel_trades = 'no'
        if cancel_trades == 'yes':
            # Cancel all and trade market
            api.cancel_all()
            balance = int(api.balance()['stock'])
            print('balance:', balance)
            if balance > 0:
                buy_order = api.submit(float(1.0), balance, 'sell', 'GTC')
            if balance < 0:
                buy_order = api.submit(float(1000.0), -balance, 'buy', 'GTC')

        # Sleep for 1 second
        time.sleep(1)

        # Get data
        try:
            tradebook = api.orderbook()
        except:
            time.sleep(1)
            tradebook = api.orderbook()
        low_ask = float(tradebook['sell'][0][0])
        high_bid = float(tradebook['buy'][-1][0])

        # Calculate spread
        spread = float(round((low_ask / high_bid - 1) * 100,2))
        print(spread)
        print(low_ask)
        print(high_bid)

        # Check if spread is high enough
        if spread > self.min_spread:
            print('Trade initiated! Spread:', spread)
            buyprice = float(round(high_bid + 0.1,1))
            sellprice = float(round(low_ask - 0.1,1))
            buy_order = api.submit(buyprice, 5, 'buy', 'GTC') # Put in buy or sell order
            sell_order = api.submit(sellprice, 5, 'sell', 'GTC') # Put in buy or sell order

            # Sleep 1 second
            time.sleep(1)

            # Get sell id
            buy_id = buy_order['order']['id']
            buy_fill = buy_order['order']['filled']
            sell_id = sell_order['order']['id']
            sell_fill = sell_order['order']['filled']

            while buy_fill != 5 and sell_fill != 5:
                print(buy_fill, sell_fill)
                print(buy_id, sell_id)
                # Get data
                time.sleep(1)
                tradebook = api.orderbook()

                print(tradebook)
                low_ask = float(tradebook['sell'][0][0])
                high_bid = float(tradebook['buy'][-1][0])

                # Sleep 1 second
                time.sleep(1)

                # Get open orders
                open_orders = api.orders_active()
                open_orders_list = []
                for orders in open_orders:
                    id = orders['id']
                    if id == sell_id:
                        sell_fill = orders['filled']
                        open_orders_list.append('sell')
                    elif id == buy_id:
                        buy_fill = orders['filled']
                        open_orders_list.append('buy')
                    if 'sell' not in open_orders_list:
                        sell_fill = 5
                    if 'buy' not in open_orders_list:
                        sell_fill = 5

                # If sell isn't filled
                if (sellprice - low_ask) / low_ask * 100 > self.max_loss and sell_fill != int(5):
                    try: 
                        api.cancel(sell_id)
                        print('Sell orer cancelled')
                        sellprice = float(round(low_ask - 0.1,1))
                        sell_order = api.submit(sellprice, 5, 'sell', 'GTC')['order']['id']
                        
                        # Sleep 1 second
                        time.sleep(1)

                        # Get open orders
                        open_orders = api.orders_active()
                        open_orders_list = []
                        for orders in open_orders:
                            id = orders['id']
                            if id == sell_id:
                                sell_fill = orders['filled']
                                open_orders_list.append('sell')
                            elif id == buy_id:
                                buy_fill = orders['filled']
                                open_orders_list.append('buy')
                            if 'sell' not in open_orders_list:
                                sell_fill = 5
                            if 'buy' not in open_orders_list:
                                sell_fill = 5

                    except:
                        print('sell order filled?')

                # If buy isn't filled
                if (high_bid - buyprice) / buyprice * 100 > self.max_loss and buy_fill != int(5):
                    try:
                        api.cancel(buy_id)
                        print('Buy order cancelled')
                        buyprice = float(round(high_bid - 0.1,1))
                        buy_order = api.submit(buyprice, 5, 'buy', 'GTC')['order']['id']
                        
                        # Sleep 1 second
                        time.sleep(1)

                        # Get open orders
                        open_orders = api.orders_active()
                        open_orders_list = []
                        for orders in open_orders:
                            id = orders['id']
                            if id == sell_id:
                                sell_fill = orders['filled']
                                open_orders_list.append('sell')
                            elif id == buy_id:
                                buy_fill = orders['filled']
                                open_orders_list.append('buy')
                            if 'sell' not in open_orders_list:
                                sell_fill = 5
                            if 'buy' not in open_orders_list:
                                sell_fill = 5

                    except:
                        print('buy order filled?')

            # Sleep 1 second
            time.sleep(1)

        time.sleep(1)

mm = MarketMaker()
#exit()
#api.balance()
#api.submit(float(1100.0), 5, 'sell', 'GTC')
#api.submit(float(1100.0), 5, 'sell', 'GTC')
#a = api.orders_active()
#print(a)
#exit()
#print('order submitted')
while 1 > 0:
    mm.trade()
    import Fairprice
