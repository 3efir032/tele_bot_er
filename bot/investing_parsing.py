import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import json

class Futuresmarket:
    URL = 'https://ru.investing.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    @classmethod
    def contents(cls):
        full_page_usd = requests.get(cls.URL, headers=cls.headers)
        soup = BeautifulSoup(full_page_usd.content, 'lxml')
        return soup

    def __init__(self, USD='None', EUR='None'):
        self.USD = self.get_price_usd()
        self.percentusd = self.get_percent_usd()
        self.EUR = self.get_price_eur()
        self.percenteur = self.get_percent_eur()

    def get_price_usd(self):
        try:
            invest_usd = self.contents().find("div", class_="quotesBarContentWrapper").find("span",
                                                                                            id=f"qb_pair_last_2186").text

            return invest_usd

        except AttributeError:
            return 'NoneType'

    def get_percent_usd(self):
        try:
            percent_usd = self.contents().find("div", class_="quotesBarContentWrapper").find("span",
                                                                                  id=f"qb_pair_change_2186").text
            return percent_usd

        except AttributeError:
            return '%'

    def get_price_eur(self):
        try:
            invest_eur = self.contents().find("div", class_="quotesBarContentWrapper").find("span", id=f"qb_pair_last_1691").text
            return invest_eur

        except AttributeError:
            return 'NoneType'

    def get_percent_eur(self):
        try:
            percent_eur = self.contents().find("div", class_="quotesBarContentWrapper").find("span",
                                                                                  id=f"qb_pair_change_1691").text
            return percent_eur

        except AttributeError:
            return '%'

def write(data, filename): # Запись файла JSON
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 2)

def write1_json():
    data = {
        "FUTURESNOW": [],
    }
    data["FUTURESNOW"].append(Futuresmarket().__dict__)
    write(data, 'futuresmarket.json')

def main():
    write1_json()

if __name__ == '__main__':
    main()