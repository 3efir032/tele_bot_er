from pycbrf.toolbox import ExchangeRates, Banks
import datetime as dt


def world_money():
    rates = ExchangeRates()
    USD = round(rates['USD'].value, 2)
    EUR = round(rates['EUR'].value, 2)
    AMD = round(rates['AMD'].value, 2)
    CNY = round(rates['CNY'].value, 2)
    GBP = round(rates['GBP'].value, 2)
    CHF = round(rates['CHF'].value, 2)
    JPY = round(rates['JPY'].value, 2)
    return USD, EUR, AMD, CNY, GBP, CHF, JPY


def info_money():
    USD, EUR, AMD, CNY, GBP, CHF, JPY = world_money()
    CNY1 = int(CNY)/10
    JPY1 = JPY/100
    money_now = f'🇨🇳 CNY/RUB: {CNY1}\n' \
                f'🇬🇧 GBP/RUB: {GBP}\n' \
                f'🇨🇭 CHF/RUB: {CHF}\n' \
                f'🇯🇵 JPY/RUB: {JPY1}\n ' \

    return money_now


def info_money_usd():
    USD, EUR, AMD, CNY, GBP, CHF, JPY = world_money()
    AMD1 = AMD/10
    usd_eur_amd = f'🇺🇸 USD/RUB: {USD}\n' \
                  f'🇪🇺 EUR/RUB: {EUR}\n' \
                  f'🇦🇲 AMD/RUB: {AMD1}\n' \

    return usd_eur_amd


def main():
    info_money_usd()
    info_money()

if __name__ == '__main__':
    main()

# https://pythonz.net/articles/64/ - Источник

# Запрашиваем данные на 26-е июня.
# rates = ExchangeRates('2022-06-21')

# dt_string = dt.datetime.now().strftime("%Y-%m-%d") # Текущая дата

# rates.date_requested  # 2016-06-26 00:00:00
# rates.date_received  # 2016-06-25 00:00:00
# 26-е был выходной, а курс на выходные установлен 25-го
# rates.dates_match  # False

# Список всех курсов валют на день доступ в rates.rates.

# Поддерживаются разные идентификаторы валют:
# rates['USD'].name  # Доллар США
# rates['R01235'].name  # Доллар США
# rates['840'].name  # Доллар США

# Вот, что внутри объекта ExchangeRate:


'''
    ExchangeRate(
        id='R01235',
        name='Доллар США',
        code='USD',
        num='840',
        value=Decimal('65.5287'),
        par=Decimal('1'),
        rate=Decimal('65.5287'))
'''
