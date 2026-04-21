import socket
import os
import time
from multiprocessing import Process

# Налаштування зв'язку
HOST = '127.0.0.1'  # Локальна адреса (localhost)
PORT = 65432        # Порт для підключення

def run_server():
    """Функція сервера, яка очікує число і повертає його подвоєним"""
    # Створюємо TCP-сокет (AF_INET - IPv4, SOCK_STREAM - TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[Сервер] Запущено. Очікування підключення на {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"[Сервер] Підключено клієнта з адресою: {addr}")
            # Отримуємо дані (байти) та декодуємо в рядок
            data = conn.recv(1024).decode()
            if data:
                number = int(data)
                result = number * 2
                print(f"[Сервер] Отримано число {number}. Відправляю результат: {result}")
                # Відправляємо результат назад клієнту
                conn.sendall(str(result).encode())

def run_client():
    """Функція клієнта, яка відправляє число серверу"""
    time.sleep(1)  # Затримка, щоб сервер встиг запуститися
    number_to_send = 42  # Число для відправки
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[Клієнт] Спроба підключення до сервера...")
        s.connect((HOST, PORT))
        print(f"[Клієнт] Відправка числа: {number_to_send}")
        s.sendall(str(number_to_send).encode())
        
        # Очікуємо відповідь
        response = s.recv(1024).decode()
        print(f"[Клієнт] Отримано відповідь від сервера: {response}")

if __name__ == "__main__":
    # Створюємо два окремих процеси для демонстрації IPC
    server_process = Process(target=run_server)
    client_process = Process(target=run_client)

    # Запуск процесів
    server_process.start()
    client_process.start()

    # Очікування завершення
    client_process.join()
    server_process.join()
    print("\n[Система] Взаємодія завершена успішно.")