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


text = "черепаха"
encrypted = caesar_encrypt(text, 4)
print(encrypted)  # фтузхеффмхезрсмй