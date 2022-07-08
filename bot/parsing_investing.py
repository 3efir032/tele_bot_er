import requests as req
from bs4 import BeautifulSoup

USD = 'https://ru.investing.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

full_page_usd = req.get(USD, headers=headers)
soup = BeautifulSoup(full_page_usd.content, 'lxml')

invest_usd = soup.find("div", class_="quotesBarContentWrapper").find("span", id = "qb_pair_last_2186").text
percent_usd = soup.find("div", class_="quotesBarContentWrapper").find("span", id = "qb_pair_change_2186").text
info_usd = f'🇺🇸 USD/RUB: {invest_usd} | {percent_usd}'

invest_eur = soup.find("div", class_ = "quotesBarContentWrapper").find("span", id = "qb_pair_last_1691").text
percent_eur = soup.find("div", class_ = "quotesBarContentWrapper").find("span", id = "qb_pair_change_1691").text
info_eur = f'🇪🇺 EUR/RUB: {invest_eur} | {percent_eur}'

