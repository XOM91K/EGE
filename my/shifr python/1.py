def xor_encrypt_decrypt(text: str, key: str):
    result = []  
    key_bytes = key.encode()
    for i, char in enumerate(text.encode()):
        result.append(char ^ key_bytes[i % len(key_bytes)])
        # result = [41, 39, 47, 45, 45]
    return bytes(result)
# Задание 1
encrypted = xor_encrypt_decrypt("PYTHON", "CODE")
print(encrypted)  #b'\x13\x16\x10\r\x0c\x01'
# Задание 2
decrypted = xor_encrypt_decrypt(b'\x12\x07\x1c'.decode(), "tro")
print(decrypted.decode())  # fus