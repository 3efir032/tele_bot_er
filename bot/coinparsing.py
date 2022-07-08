import requests
from bs4 import BeautifulSoup

'''ОПИСАНИЕ'''


def url_wedside(link_coin):
    link = f'https://ru.investing.com/crypto/{link_coin}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    try:
        full_page_coin = requests.get(link, headers=headers)
        soup = BeautifulSoup(full_page_coin.content, 'lxml')
        return soup
    except requests.exceptions.ConnectionError:
        return '443'


def parseng_coin(soup, idcoin):
    price_coin = soup.find("div", class_="fullHeaderTwoColumnPage--top cryptoTopColumn").find("span",
                                                                                              class_="inlineblock").find(
        "span", class_=f"pid-{idcoin}-last").text
    return price_coin


def start(namecoin, idcoin):
    url = url_wedside(namecoin)
    if url != '443':
        return parseng_coin(url, idcoin)
    else:
        return 'error'


def coinprice():
    bitcoin = start('bitcoin', '1057391')
    ethereum = start('ethereum', '1061443')
    tether = start('tether', '1061453')
    binance_usd = start('binance-usd', '1177192')
    bnb = start('bnb', '1061448')
    return bitcoin, ethereum, tether, binance_usd, bnb


def infocoin():
    bitcoin, ethereum, tether, binance_usd, bnb = coinprice()
    coin_info = f"➖ 1 BTC - {bitcoin}$\n" \
                f"➖ 1 ETH - {ethereum}$\n" \
                f"➖ 1 BUSD - {binance_usd}$\n" \
                f"➖ 1 USDT - {tether}$\n" \
                f"➖ 1 BNB - {bnb}$\n"

    return coin_info


if __name__ == '__main__':
    infocoin()

# BTC 1057391
# ETH 1061443
# BUSD 1177192
# USDT 1061453
# BNB 1061448
