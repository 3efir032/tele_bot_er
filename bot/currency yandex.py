import requests
from bs4 import BeautifulSoup

BTC = 'https://yandex.ru/news/quotes/60000'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
full_page_btc = requests.get(BTC, headers=headers)
soup_btc = BeautifulSoup(full_page_btc.content, 'html.parser')
convert = soup_btc.findAll("div", {"class": "news-stock-graph__content-title-rate-value"})
btc_now = convert[-1].text