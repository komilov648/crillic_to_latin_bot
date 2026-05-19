import telebot
import os
from dotenv import load_dotenv
from transliterate import to_cyrillic, to_latin

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum, botimizga xush kelibsiz")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# print(message)
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else:
		bot.reply_to(message, to_latin(text))
	
bot.infinity_polling()

# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))