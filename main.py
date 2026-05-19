import telebot
import os

from detect_script import detect_script
from transliterate import to_cyrillic, to_latin
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(
        message,
        "Assalom alaykum! Menga lotin yoki kiril matn yuboring.\n"
        "Lotin → Kiril yoki Kiril → Lotin ga aylantiraman."
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text.strip()
	script = detect_script(msg)

	if script == 'latin':
		res = to_cyrillic(msg)
	else:	
		res = to_latin(msg)
	bot.reply_to(message, res)
	
bot.infinity_polling()

# text = input("Enter text: ")
# if text.isascii():
#     print(to_cyrillic(text))
# else:    print(to_latin(text))   