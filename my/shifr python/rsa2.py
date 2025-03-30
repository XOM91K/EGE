import rsa

# Генерируем пару ключей
(pub_key, priv_key) = rsa.newkeys(512)  # 512 бит (для примера, в реальности используйте ≥2048)

# Шифруем открытым ключом
message = "Hello, World!".encode()
encrypted = rsa.encrypt(message, pub_key)
print("Зашифровано:", encrypted.hex())

# Дешифруем закрытым ключом
decrypted = rsa.decrypt(encrypted, priv_key)
print("Расшифровано:", decrypted.decode())