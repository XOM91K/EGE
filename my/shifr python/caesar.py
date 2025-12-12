def caesar_encrypt(text, shift):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    for char in text.lower():
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += char
    return result
text = "всош{вот_он_флаг}"
encrypted = caesar_encrypt(text, 3)
# руфтэл озщ к увгнб  острый меч и сабля
print(encrypted)  # ыйфйудщд
# alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# s = 'ряд'
# print(alphabet.index(s[0]), alphabet.index(s[1]), alphabet.index(s[2]),)