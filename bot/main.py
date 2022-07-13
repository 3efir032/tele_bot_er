from currency import info_money_usd, info_money
import schedule
import time
import telebot
from telebot import types
from tokenbot import token
from data import fururesnow, coin


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def startbot(message):
    keyboard_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_one = types.KeyboardButton('🇷🇺RUS')
    item_two = types.KeyboardButton('💲Crypto')
    item_tree = types.KeyboardButton('🌏МИР')
    keyboard_reply.add(item_one, item_two, item_tree)
    bot.send_message(message.chat.id,
                     f'👋 Привет. Я — чат-бот.\nПоказываю курс фиатных валют, криптовалют и акции.',
                     reply_markup=keyboard_reply)


    
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == '🇷🇺RUS':
        usd_now = info_money_usd()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('КУРС НА СРОЧНОМ РЫНКЕ', callback_data='good')
        markup.add(item1)
        bot.send_message(message.chat.id, usd_now, reply_markup=markup)

    elif message.text == '💲Crypto':
        coin_now = coin()
        bot.send_message(message.chat.id, coin_now)

    elif message.text == '🌏МИР':
        money_now = info_money()
        bot.send_message(message.chat.id, money_now)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                furures_now = fururesnow()
                bot.send_message(call.message.chat.id, furures_now)
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    bot.polling(none_stop=True)
