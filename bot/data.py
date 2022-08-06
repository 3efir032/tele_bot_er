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
    btc = coin['COIN'][0]
    etc = coin['COIN'][1]
    usdt = coin['COIN'][2]
    bnb = coin['COIN'][3]
    #return f"🔹1 BTC = {btc}\n🔹1 ETC = {etc}\n🔹1 USDT = {usdt}\n🔹1 BNB = {bnb}"
    return f'🔹{btc}\n🔹{etc}\n🔹{usdt}\n🔹{bnb}'

print(coin())