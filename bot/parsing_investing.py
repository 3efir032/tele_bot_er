import requests as req
from bs4 import BeautifulSoup

'''ОПИСАНИЕ - парсит курс валют с биржи
Код работает медленно
'''


def url_webside():
    USD = 'https://ru.investing.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    try:
        full_page_usd = req.get(USD, headers=headers)
        soup = BeautifulSoup(full_page_usd.content, 'lxml')
        return soup
    except requests.exceptions.ConnectionError:
        return '443'


def parsing_money(soup, idmoney):
    invest_usd = soup.find("div", class_="quotesBarContentWrapper").find("span", id=f"qb_pair_last_{idmoney}").text
    percent_usd = soup.find("div", class_="quotesBarContentWrapper").find("span", id=f"qb_pair_change_{idmoney}").text
    return invest_usd, percent_usd


def start(idmoney):
    url = url_webside()
    if url != '443':
        return parsing_money(url, idmoney)
    else:
        return 'error'


def price():
    usd_price, usd_percent = start(2186)
    eur_price, eur_percent = start(1691)
    info_price_money = f"🇺🇸 USD/RUB: {usd_price} | {usd_percent}\n" \
                       f"🇪🇺 EUR/RUB: {eur_price} | {eur_percent}"
    return info_price_money


if __name__ == '__main__':
    price()

# USD - 2186
# EUR - 1691
