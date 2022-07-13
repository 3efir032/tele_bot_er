import requests
from bs4 import BeautifulSoup
import json
import schedule
import time
"""ОПИСАНИЕ"""

class Coin:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    def __init__(self, coin_name='bitcoin', numcoin='1057391'):
        self.url = f'https://ru.investing.com/crypto/{coin_name}'
        self.numcoin = numcoin
        self.price = self.get_btc()

    def get_btc(self):
        full_page_btc = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(full_page_btc.content, 'lxml')
        price = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("div", class_="inlineblock").find("div", class_="top").find("span", class_="inlineblock")
        return price
    def __str__(self):
        return f"{self.price}"

c = Coin()
print(c)