import telebot
import os
from dotenv import load_dotenv
from transliterate import to_cyrillic, to_latin


load_dotenv() 



TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
     bot.reply_to(message, "Asalamu alaykum, botimizga xush kelibsiz! ")
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
     text = message.text
     if text.isascii():   
          bot.reply_to(message, to_cyrillic(text))
     else:
          bot.reply_to(message, to_latin(text))
 
bot.infinity_polling()





# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Salom!")

# @bot.message_handler(func=lambda message: True)
# def convert_text(message):

#     text = message.text

#     try:
#         # Latin -> Kirill
#         if text.isascii():
#             result = to_cyrillic(text)
#         else:
#             # Kirill -> Latin
#             result = to_latin(text)

#         bot.reply_to(message, result)

#     except Exception as e:
#         bot.reply_to(message, f"Xato: {e}")

# bot.infinity_polling()


# import telebot
# from transliterate import to_cyrillic, to_latin

# TOKEN = "TOKEN"
# bot = telebot.TeleBot(TOKEN)




# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))    