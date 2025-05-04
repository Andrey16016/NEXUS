import time
import telebot
import colorama
from colorama import Fore
import os

os.system("clear")

colorama.init()
print (Fore.YELLOW + "")


print ("ОБЩАЙСЯ С ЮЗЕРАМИ ТГ ПРЯМО ИЗ КОНСОЛИ")
print ("Главное чтобы они нажали /start в боте")
print ("")

#script

def bot():
    token = input("Токен бота:")
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи. ')
        while True:
            @bot.message_handler(content_types=["text"])
            def handle_text(message):
                print ("Noname:", message.text)
                n = input("Вы:")
                bot.send_message(m.chat.id, n)
    bot.polling(none_stop=True, interval=0)


bot()


#the end
print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")








