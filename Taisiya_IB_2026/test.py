# s = 'abracadabra'
# print(set(s))
# import hashlib
# print(hashlib.pbkdf2_hmac())
import hashlib

def derive_key_pbkdf2(password, salt_hex, iterations):
    # верни hex 32-байтового ключа (PBKDF2-HMAC-SHA256)
    return hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt_hex), iterations, 32).hex()
print(derive_key_pbkdf2("netherite", "0a0b0c0d0e0f1011", 1000))