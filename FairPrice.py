import requests
from bs4 import BeautifulSoup
import pandas as pd

class PinneappleFairPrice():
    def __init__(self):

        # Api keys
        self.url = "https://orderbookz.com/company"

    def fairPrice(self):
        page = requests.get(self.url)

        soup = BeautifulSoup(page.text, 'lxml')
        table = soup.find("table")

        totalProfit = 0

        for j in table.find_all("tr")[1:]:
         row_data = j.find_all("td")[2:]
         row = [i.text for i in row_data]
         profit = row[0]

         totalProfit += float(profit)

        fairPrice = (100000+totalProfit)/1000

        return fairPrice

fp = PinneappleFairPrice()

output = fp.fairPrice()

print(output)
