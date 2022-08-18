import telebot
import json
from token import token

bot = telebot.TeleBot(token)
with open('cards.json', 'r'):


@bot.message_handler(commands=['start'])
def dialog_start(message):
