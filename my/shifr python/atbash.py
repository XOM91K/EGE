def atbash_decrypt(text):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    reversed_alphabet = alphabet[::-1]
    result = ""

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            result += reversed_alphabet[index]
        else:
            result += char

    return result


encrypted_text = "всош{хороший_флажок}"
decrypted = atbash_decrypt(encrypted_text)
print(decrypted)  # сйптцосчсцпсцо