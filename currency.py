import requests
import telebot
from telebot import types

bot = telebot.TeleBot("5824495970:AAHQ5_ZB1-MQrMzZoUwFiuFYCXLe1W4pQa4")

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

Usd = str(res['Valute']["USD"]['Name']) + ' = ' + str(res['Valute']["USD"]['Value'])
Eur = str(res['Valute']["EUR"]['Name']) + ' = ' + str(res['Valute']["EUR"]['Value'])

@bot.message_handler(commands=['start'])
def start(message):
    global Usd, Eur
    markup = types.InlineKeyboardMarkup(row_width = 2)
    button1 = types.InlineKeyboardButton("USD", callback_data = 'Usd')
    button2 = types.InlineKeyboardButton("EUR", callback_data = 'Eur')
    markup.add(button1, button2)

    bot.send_message(message.chat.id, 'Выбери в меню валюту, и я покажу ее курс.\nЧтобы показать меню еще раз, введи " /start "', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Usd':
            bot.send_message(call.message.chat.id, Usd)
        elif call.data == 'Eur':
            bot.send_message(call.message.chat.id, Eur)

bot.polling()

