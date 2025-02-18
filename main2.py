
encrypted_password = "\x33\x20\x34\x05\x15\x04\x21\x67\x13\x35\x67\x37\x07\x32"  # Замените на извлечённое значение
decrypted_password = bytes([(~(int(c, 16) ^ 0x57)) & 0xff for c in encrypted_password])
print(decrypted_password.decode())