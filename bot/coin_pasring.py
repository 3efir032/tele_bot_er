import requests
from bs4 import BeautifulSoup
import json

"""ОПИСАНИЕ - ПАРСИН КРИПТЫ С САЙТА ru.investing.com"""


def url_coin(namecoin):
    url = f'https://ru.investing.com/crypto/{namecoin}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    full_page_coin = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page_coin.content, 'lxml')
    return namecoin, soup


def price_coin(namecoin):
    namecoin, soup = url_coin(namecoin)
    price = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("div",
                                                                                         class_="inlineblock").find(
        "div", class_="top").find("span", class_="inlineblock").text
    return f"1 {namecoin.title()} = {price[2:]}"


def write(data, filename):  # Запись файла JSON
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def write_json():
    data = {
        "COIN": [],
    }
    data["COIN"].append(price_coin('bitcoin'))
    data["COIN"].append(price_coin('ethereum'))
    data["COIN"].append(price_coin('tether'))
    data["COIN"].append(price_coin('bnb'))
    write(data, 'price_coin.json')


def main():
    write_json()


if __name__ == '__main__':
    main()
