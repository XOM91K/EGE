from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # AES-128
print('key:', key)
# Создаем шифр
cipher = AES.new(key, AES.MODE_ECB)
# Шифруем текст (длина должна быть кратна 16 байтам)
text = "Hello, World!123".encode()  # 16 символов
encrypted = cipher.encrypt(text)
print("Зашифровано:", encrypted.hex())

# Дешифруем
decrypted = cipher.decrypt(encrypted)
print("Расшифровано:", decrypted.decode())
