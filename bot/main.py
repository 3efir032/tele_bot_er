from currency import info_money_usd, info_money
from parsing_investing import info_usd, info_eur
from coinparsing import coin
import telebot
from telebot import types
from tokenbot import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def startbot(message):
    keyboard_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_one = types.KeyboardButton('🇷🇺RUS')
    item_two = types.KeyboardButton('💲Crypto')
    item_tree = types.KeyboardButton('🌏МИР')
    item_four = types.KeyboardButton('📈Акции')
    keyboard_reply.add(item_one, item_two, item_tree, item_four)
    bot.send_message(message.chat.id,
                     f'👋 Привет Я — чат-бот.\nПоказываю курс фиатных валют, криптовалют и акции.',
                     reply_markup=keyboard_reply)


@bot.message_handler(content_types=['text'])
def get_text(message):

    if message.text == '🇷🇺RUS':
        usd_now = info_money_usd()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('КУРС НА БИРЖЕ', callback_data='good')
        markup.add(item1)
        bot.send_message(message.chat.id, usd_now, reply_markup=markup)

    elif message.text == '💲Crypto':
        coin_now = coin()
        bot.send_message(message.chat.id, coin_now)

    elif message.text == '🌏МИР':
        money_now = info_money()
        bot.send_message(message.chat.id, money_now)

    elif message.text == '📈Акции':
        pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                info_bi = f"{info_usd}\n{info_eur}"
                bot.send_message(call.message.chat.id, info_bi)
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    bot.polling(none_stop=True)