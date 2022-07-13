import requests
from bs4 import BeautifulSoup
import json
import schedule
import time


class Coin:
    URLBTC = "https://ru.investing.com/crypto/bitcoin"
    URLETC = "https://ru.investing.com/crypto/ethereum"
    URLBUSD = "https://ru.investing.com/crypto/binance-usd"
    URLUSDT = "https://ru.investing.com/crypto/tether"
    URLBNB = "https://ru.investing.com/crypto/bnb"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    def __init__(self):
        self.btc = self.get_btc()
        self.etc = self.get_etc()
        self.busd = self.get_busd()
        self.usdt = self.get_usdt()
        self.bnb = self.get_bnb()

    def get_btc(self):
        full_page_btc = requests.get(self.URLBTC, headers=self.headers)
        soup = BeautifulSoup(full_page_btc.content, 'lxml')
        price_btc = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                                 class_="inlineblock").find(
            "span", class_=f"pid-1057391-last").text
        return price_btc

    def get_etc(self):
        full_page_etc = requests.get(self.URLETC, headers=self.headers)
        soup = BeautifulSoup(full_page_etc.content, 'lxml')
        price_etc = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                                 class_="inlineblock").find(
            "span", class_=f"pid-1061443-last").text
        return price_etc

    def get_busd(self):
        full_page_busd = requests.get(self.URLBUSD, headers=self.headers)
        soup = BeautifulSoup(full_page_busd.content, 'lxml')
        price_busd = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                                  class_="inlineblock").find(
            "span", class_=f"pid-1177192-last").text
        return price_busd

    def get_usdt(self):
        full_page_usdt = requests.get(self.URLUSDT, headers=self.headers)
        soup = BeautifulSoup(full_page_usdt.content, 'lxml')
        price_usdt = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                                  class_="inlineblock").find(
            "span", class_=f"pid-1061453-last").text
        return price_usdt

    def get_bnb(self):
        full_page_bnb = requests.get(self.URLBNB, headers=self.headers)
        soup = BeautifulSoup(full_page_bnb.content, 'lxml')
        price_bnb = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                                 class_="inlineblock").find(
            "span", class_=f"pid-1061448-last").text
        return price_bnb


def write(data, filename):  # Запись файла JSON
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def write_json():
    data = {
        "COIN": [],
    }
    data["COIN"].append(Coin().__dict__)
    write(data, 'price_coin.json')


def main():
    write_json()


if __name__ == '__main__':
    main()
