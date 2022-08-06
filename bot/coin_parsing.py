import requests
from bs4 import BeautifulSoup
import json
import schedule
import time

"""ОПИСАНИЕ"""


class Coin:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    def __init__(self, coin_name='bitcoin'):
        self.url = f'https://ru.investing.com/crypto/{coin_name}'
        self.price = self.get_btc()

    def get_btc(self):
        full_page_btc = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(full_page_btc.content, 'lxml')
        price = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("div",
                                                                                             class_="inlineblock").find(
            "div", class_="top").find("span", class_="inlineblock").text
        return price

def write(data, filename): # Запись файла JSON
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 2)

def write_json():
    data = {
        "COIN": [],
    }

    data["COIN"].append(Coin().__dict__)
    data["COIN"].append(Coin('ethereum').__dict__)
    data["COIN"].append(Coin("tether").__dict__)
    data["COIN"].append(Coin("bnb").__dict__)
    write(data, 'price_coin.json')

def main():
    write_json()

if __name__ == '__main__':
    main()