# text = "Кибербезопасность"
# bytes_data = text.encode("utf-8")
# # b'\xd0\x9 ... \x81\xd1\x82\xd1\x8c'
# print(bytes_data.hex())
# # d09ad0b8d0b1...81d0bdd0bed181d182d18c
# name = "Иванов"
# bytes_name = name.encode("utf-8")
# # b'\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2'
# hex_name = bytes_name.hex()
# # d098d0b2d0b0d0bdd0bed0b2
# decoded = bytes.fromhex(hex_name).decode("utf-8")
# print(decoded)
# # Иванов
def xor_encrypt_decrypt(text: str, key: str):
    result = []
    key_bytes = key.encode()
    for i, char in enumerate(text.encode()):
        result.append(char ^ key_bytes[i % len(key_bytes)])
    # result = [41, 39, 47, 45, 45]
    return bytes(result)
# Пример
encrypted = xor_encrypt_decrypt("HELLO", "abc")
print("Зашифровано:", encrypted) # b")'/--"

decrypted = xor_encrypt_decrypt(encrypted.decode("utf-8"), "abc")
print("Расшифровано:", decrypted.decode("utf-8")) # HELLO