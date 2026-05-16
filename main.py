import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "8219964547:AAHbMdFCsvJqoQhHSLHR8NTBpGAFeuI5zN0"
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


# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))    