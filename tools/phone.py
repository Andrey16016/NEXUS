import time
import os
import colorama
from colorama import Fore
import random


os.system("clear")
#hello world
colorama.init()

print ("ГЕНЕРИРУЙ НОМЕРА")
print ("")


print (Fore.GREEN + "")

def gen():
    kol = input("[=] Количество номеров:")
    time.sleep(1)
    print ("Номера...")
    for h in range(int(kol)):
        phone = random.randint(79000000000, 79999999999)
        print (phone)
 #       print (Fore.YELLOW + "")
   # p = input("Нажми enter")

gen()


print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")
