def vigenere_cipher(text, key, language):
    result = []
    key_length = len(key)
    key_index = 0

    if language == 'RU':
        # Русский алфавит с Ё (33 буквы)
        upper_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lower_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet_size = 33
    elif language == 'EN':
        # Английский алфавит (26 букв)
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_size = 26
    else:
        return "Неверно указан язык. Используйте 'RU' или 'EN'."

    for char in text:
        if language == 'RU' and char in upper_alphabet:
            # Обработка русских заглавных букв (включая Ё)
            key_char = key[key_index % key_length].upper()
            if key_char in upper_alphabet:
                original_pos = upper_alphabet.index(char)
                key_pos = upper_alphabet.index(key_char)
                new_pos = (original_pos + key_pos) % alphabet_size
                result.append(upper_alphabet[new_pos])
                key_index += 1
            else:
                result.append(char)
        elif language == 'RU' and char in lower_alphabet:
            # Обработка русских строчных букв (включая ё)
            key_char = key[key_index % key_length].lower()
            if key_char in lower_alphabet:
                original_pos = lower_alphabet.index(char)
                key_pos = lower_alphabet.index(key_char)
                new_pos = (original_pos + key_pos) % alphabet_size
                result.append(lower_alphabet[new_pos])
                key_index += 1
            else:
                result.append(char)
        elif language == 'EN' and char.isupper() and char in upper_alphabet:
            # Обработка английских заглавных букв
            key_char = key[key_index % key_length].upper()
            if key_char in upper_alphabet:
                original_pos = upper_alphabet.index(char)
                key_pos = upper_alphabet.index(key_char)
                new_pos = (original_pos + key_pos) % alphabet_size
                result.append(upper_alphabet[new_pos])
                key_index += 1
            else:
                result.append(char)
        elif language == 'EN' and char.islower() and char in lower_alphabet:
            # Обработка английских строчных букв
            key_char = key[key_index % key_length].lower()
            if key_char in lower_alphabet:
                original_pos = lower_alphabet.index(char)
                key_pos = lower_alphabet.index(key_char)
                new_pos = (original_pos + key_pos) % alphabet_size
                result.append(lower_alphabet[new_pos])
                key_index += 1
            else:
                result.append(char)
        else:
            # Все остальные символы (не буквы или буквы другого алфавита)
            result.append(char)

    return ''.join(result)


def generate_html(text, key, language, result):
    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Результат шифрования Виженера</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                padding: 20px;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            .result {{
                background-color: #f0f8ff;
                padding: 15px;
                border-left: 4px solid #4682b4;
                margin: 10px 0;
            }}
            .info {{
                margin-bottom: 20px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Результат шифрования Виженера</h1>

            <div class="info">
                <p><strong>Исходный текст:</strong> {text}</p>
                <p><strong>Ключ:</strong> {key}</p>
                <p><strong>Язык:</strong> {language}</p>
            </div>

            <div class="result">
                <h3>Зашифрованный текст:</h3>
                <p>{result}</p>
            </div>

            <div class="info">
                <h3>Примечания:</h3>
                <p>Для русского языка (RU) используется алфавит из 33 букв (А-Я, включая Ё):</p>
                <table>
                    <tr><th>Позиция</th><th>Буква</th></tr>
                    <tr><td>0</td><td>А</td></tr>
                    <tr><td>1</td><td>Б</td></tr>
                    <tr><td>...</td><td>...</td></tr>
                    <tr><td>6</td><td>Ё</td></tr>
                    <tr><td>...</td><td>...</td></tr>
                    <tr><td>32</td><td>Я</td></tr>
                </table>
                <p>Для английского языка (EN) используется алфавит из 26 букв (A-Z):</p>
                <table>
                    <tr><th>Позиция</th><th>Буква</th></tr>
                    <tr><td>0</td><td>A</td></tr>
                    <tr><td>1</td><td>B</td></tr>
                    <tr><td>...</td><td>...</td></tr>
                    <tr><td>25</td><td>Z</td></tr>
                </table>
                <p>Шифрование применяется только к буквам выбранного алфавита, остальные символы остаются без изменений.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


def main():
    text = 'My secret message' # текст
    key = 'brown' # ключ
    language = 'EN' # EN RU

    if language not in ['RU', 'EN']:
        print("Ошибка: язык должен быть либо 'RU', либо 'EN'")
        return

    encrypted_text = vigenere_cipher(text, key, language)

    html_output = generate_html(text, key, language, encrypted_text)

    # Сохраняем результат в файл
    with open("vigenere_result.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("Результат сохранен в файл vigenere_result.html")


if __name__ == "__main__":
    main()