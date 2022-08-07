import requests
from bs4 import BeautifulSoup
import json

"""ОПИСАНИЕ - ПАРСИН КРИПТЫ С САЙТА ru.investing.com"""


class Coin:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    def __init__(self, coin_name='bitcoin', num_coin='1057391'):
        self.url = f'https://ru.investing.com/crypto/{coin_name}'
        self.num = num_coin
        self.price = self.getcoin()
        self.persent = self.get_persent()

    def contents(self):
        full_page_btc = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(full_page_btc.content, 'html.parser')
        return soup

    def getcoin(self):
        price = self.contents().find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("div", class_="inlineblock").find("span", class_="inlineblock" ).find('span', id="last_last").text
        return price

    def get_persent(self):
        try:
            persent = self.contents().find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("div", class_="inlineblock").find("span", class_="arial_20").text
            return persent
        except AttributeError:
            return 'None-persent'

def write(data, filename): # Запись файла JSON
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 2)

def write_json():
    data = {
        "COIN": [],
    }

    data["COIN"].append(Coin('bitcoin', '1057391').__dict__)
    data["COIN"].append(Coin('ethereum', '1061443').__dict__)
    data["COIN"].append(Coin("tether", '1061453').__dict__)
    data["COIN"].append(Coin("bnb", '1061448').__dict__)
    write(data, 'price_coin.json')

def main():
    write_json()

if __name__ == '__main__':
    main()