import time
import os
import random
import colorama
from colorama import Fore

colorama.init()


print (Fore.YELLOW + "")
#script


def genip():
    
    ips = input('Кол-во:')

    print (Fore.RED + "")


    print ('1. Запись в txt файл')
    print ('2. Вывод в консоль')

    kuda = input('>')
    

    if kuda == "1":
        
        for i in range(int(ips)):
            with open("ip/ipexit.txt", "w") as file:
                for i in range(int(ips)):
                    ip_address = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
                    file.write(str(ip_address) + "\n")
                    print (Fore.YELLOW + 'Ip Адресс записан!')
                    
        print (Fore.BLUE + "Ip Адреса записаны в файл (ipexit)")
    #    time.sleep(5)

    if kuda == "2":

        for i in range(int(ips)):
            ip_address = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            print("Ip:", ip_address)
        print (Fore.GREEN + "Готово")
  #      time.sleep(35)



genip()

print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")


