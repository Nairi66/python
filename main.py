import telebot, requests 
from telebot import apihelper
import os
import time
import logging                                                                                                                                          

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

TG_PROXY = 'https://103.241.156.250:8080'
apihelper.proxy = {'http': TG_PROXY}
bot = telebot.TeleBot("1292521216:AAFG73G8bmWVEsSVM8JRqEyGNuZsfz23Cig")

bot = telebot.TeleBot("1292521216:AAFG73G8bmWVEsSVM8JRqEyGNuZsfz23Cig")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋")
    bot.send_message(message.chat.id, "Ողջոյն, բարի գալուս յղումների կրճատման համակարգ։ ❤️❤️")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    # bot.send_message(message.chat.id, "👋")
    bot.send_message(message.chat.id, "Յղում կրճատելու համար անհրաժեշ ՝\n1․ գրել @short եւ անհրաժեշտ յղումը\n2. պատճենէլ ստացուած կրճատ յղումը եւ աւգտագործել։")

@bot.message_handler(content_types=['text'])
def url_shortener(message):
    command = message.text[:7]
    if command == "@short ":
        link_to_short = message.text.replace(command, '')
        post_url = 'http://api.xn--y9aua5byc.xn--y9a3aq/urls'
        data = {'url': link_to_short}
        x = requests.post(post_url, data = data)
        short_key = x.text[:7]
        short_url = "նա.հայ/?id=" + short_key
        text = "Ձեր կրճատած յղումը պատրաստ է։ Շնորհակալութիւն։ ❤️❤️\n"
        bot.send_message(message.chat.id, text+short_url)

bot.polling()
