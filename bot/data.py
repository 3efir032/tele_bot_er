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
    return usd, percentusd, eur, percenteur


def coin():
    coin = read('price_coin.json')
    btc = coin['COIN'][0]['btc']
    etc = coin['COIN'][0]['etc']
    busd = coin['COIN'][0]['busd']
    usdt = coin['COIN'][0]['usdt']
    bnb = coin['COIN'][0]['bnb']
    return f"➖ 1 BTC - {btc}$\n➖ 1 ETC - {etc}$\n➖ 1 BUSD - {busd}$\n➖ 1 USDT - {usdt}$\n➖ 1 BNB - {bnb}$"
