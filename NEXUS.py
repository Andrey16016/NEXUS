#Developer RESHETKA

logo = """
╭━╮╱╭┳━━━┳━╮╭━┳╮╱╭┳━━━╮
┃┃╰╮┃┃╭━━┻╮╰╯╭┫┃╱┃┃╭━╮┃
┃╭╮╰╯┃╰━━╮╰╮╭╯┃┃╱┃┃╰━━╮
┃┃╰╮┃┃╭━━╯╭╯╰╮┃┃╱┃┣━━╮┃
┃┃╱┃┃┃╰━━┳╯╭╮╰┫╰━╯┃╰━╯┃
╰╯╱╰━┻━━━┻━╯╰━┻━━━┻━━━╯
"""
#script


print ("Загрузка...")
import time
import requests
import os

os.system("clear")

print ("Проверяем Соединение с Сервером...")

r = requests.get("https://github.com")

if r.status_code == 200:
    print ("Все отличной, запускаем программу...")
    time.sleep(1)
    os.system("clear")
else:
    print ("Сервер не ответил, закрываем программу")
    time.sleep(1)
    exit()


    


    


import time
import random
import colorama
from colorama import Fore, Back, Style
#from datetime import datetime
#from art import tprint11



vers = "0.07"

os.system("clear")

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

colorama.init()
print (Fore.YELLOW + "")

#ok
            
print (Fore.RED + logo)

print ("")
print (Fore.CYAN +  'Developer: RESHETKA')
#print (Fore.YELLOW +  "_____________________________________________")
print (Fore.YELLOW + "")
mn = """
[+] 1. Поиск каталогов сайта  
[+] 2. Генератор Номеров  
[+] 3. Общение с users через бота тг  
[+] 4. Поиск SQL уязвимостей  
[+] 5. Заглушить wifi
[+] 6. Смс Telegram  
[+] 7. Генератор IP  
{+} 99. Информация о программе
[+] 0. Выход  
"""
print (mn)
print ("---------------------------------------------")
user = input("[+] Выбирай действие>")


info = f"""
Developer: @h1user

Version: {vers}


ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ v{vers}
----------------------------
Обновил софт, переписал некоторые инструменты, исправил ошибки
"""


if user == "99":
    print (Fore.BLUE + info)
    time.sleep(1)
    print ("")
    i = input("Нажмите Enter")
    os.system("clear")
    os.system("python3 NEXUS.py")

if user == "5":
    from tools import wifi

if user == "7":
    from tools import genip
    #ok
    

if user == "3":
    from tools import bot
    #ok



if user == "4":
    from tools import searchxss
    #ok

if user == "2":
    from tools import phone

if user == "0":
    exit()

if user == "6":
    from tools import smstg


#usr
if user == "1":
    from tools import catalog


#the end







                
        

    
    
    
    
    
      
    
    










    
