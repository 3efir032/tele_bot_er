import json

def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def fururesnow():
    money = read('futuresmarket.json')
    usd = money["FUTURESNOW"][0]['USD']
    percentusd = money["FUTURESNOW"][0]['percentusd']
    eur = money["FUTURESNOW"][0]['EUR']
    percenteur = money["FUTURESNOW"][0]['percenteur']
    return f"πΊπΈ USD/RUB: {usd} | {percentusd}\nπͺπΊ EUR/RUB: {eur} | {percenteur}"


def coin():
    coin = read('price_coin.json')
    btc = coin['COIN'][0]['btc']
    etc = coin['COIN'][0]['etc']
    busd = coin['COIN'][0]['busd']
    usdt = coin['COIN'][0]['usdt']
    bnb = coin['COIN'][0]['bnb']
    return f"β 1 BTC - {btc}$\nβ 1 ETC - {etc}$\nβ 1 BUSD - {busd}$\nβ 1 USDT - {usdt}$\nβ 1 BNB - {bnb}$"
