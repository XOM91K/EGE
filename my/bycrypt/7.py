import requests
import urllib.parse

def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# Получаем шифротекст
data_test = {
    "creature": "a"*16,
    "name": "b"*16
}
r = requests.post("http://ctfinf.ru:10013/login", data=data_test, allow_redirects=False)
cookie_test = r.cookies.get("session")
cipher = urllib.parse.unquote_to_bytes(cookie_test)

print("Original cookie works:")
r_test = requests.get("http://ctfinf.ru:10013/profile", cookies={"session": cookie_test})
print(r_test.text)