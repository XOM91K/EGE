import os

def generate_key(length):
    return os.urandom(length)

def vernam_encrypt(plain_text, key):
    plain_text_bytes = plain_text.encode('utf-8')
    ciphertext = bytearray()
    for p, k in zip(plain_text_bytes, key):
        ciphertext.append(p^k)

    return bytes(ciphertext)

def vernam_decrypt(ciphertext, key):
    plain_text_bytes = bytearray()
    for c, k in zip(ciphertext, key):
        plain_text_bytes.append(c^k)

    return plain_text_bytes.decode('utf-8')


message = "vsosh{h1dd3n_1n_pl41n_516h7}"
key = generate_key(len(message))
ciphertext = vernam_encrypt(message, key)
print("Зашифрованное сообщение:", ciphertext.decode('latin-1'))
decrypted_message = vernam_decrypt(ciphertext, key)
print("Расшифрованное сообщение:", decrypted_message)