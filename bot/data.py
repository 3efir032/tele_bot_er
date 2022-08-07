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
    return f"🇺🇸 USD/RUB: {usd} | {percentusd}\n🇪🇺 EUR/RUB: {eur} | {percenteur}"


def coin():
    coin = read('price_coin.json')
    btc = coin['COIN'][0]['price']
    btc_percent = coin['COIN'][0]['persent']
    etc = coin['COIN'][1]['price']
    etc_percent = coin['COIN'][1]['persent']
    usdt = coin['COIN'][2]['price']
    usdt_percent = coin['COIN'][2]['persent']
    bnb = coin['COIN'][3]['price']
    bnb_percent = coin['COIN'][3]['persent']
    return f"🔹1 BTC = {btc} | {btc_percent}\n🔹1 ETC = {etc} | {etc_percent}\n🔹1 USDT = {usdt} | {usdt_percent }\n🔹1 BNB = {bnb} | {bnb_percent}"
