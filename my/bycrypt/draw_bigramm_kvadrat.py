import random
from math import isqrt
import os


def generate_encrypted_table(symbols, word, filename="encrypted_table.html"):
    """
    Генерирует HTML-таблицу с символами, шифрует слово и сохраняет результат в файл.

    :param symbols: Список символов (длина должна быть полным квадратом).
    :param word: Слово для шифрования.
    :param filename: Имя файла для сохранения (по умолчанию 'encrypted_table.html').
    :return: Путь к сохранённому файлу и зашифрованное слово.
    """
    n = isqrt(len(symbols))
    if n * n != len(symbols):
        raise ValueError("Количество символов должно быть полным квадратом числа")

    # Перемешиваем символы и создаем таблицу
    random.shuffle(symbols)
    table = [symbols[i * n: (i + 1) * n] for i in range(n)]

    # Шифруем слово
    encrypted_word = encrypt_word(table, word)

    # Генерация HTML-кода
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Зашифрованный квадрат</title>
    <style>
        table {{
            border-collapse: collapse;
            margin: 20px;
        }}
        td {{
            border: 2px solid black;
            padding: 20px;
            font-size: 24px;
            text-align: center;
            min-width: 50px;
        }}
        .highlight {{
            background-color: yellow;
        }}
    </style>
</head>
<body>
    <h2>Квадрат {n}×{n}</h2>
    <table>
        {"".join(
        f"<tr>{''.join(f'<td>{table[i][j]}</td>' for j in range(n))}</tr>"
        for i in range(n)
    )}
    </table>
    <p><strong>Исходное слово:</strong> {''.join(word)}</p>
    <p><strong>Зашифрованное слово:</strong> {encrypted_word}</p>
</body>
</html>
    """

    # Сохранение в файл
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return os.path.abspath(filename), encrypted_word


def encrypt_word(table, word):
    """
    Шифрует слово по правилам:
    1. Разбивает на биграммы.
    2. Применяет правила замены в зависимости от расположения символов в таблице.
    """
    # Разбиваем слово на биграммы (добавляем padding, если нужно)
    if len(word) % 2 != 0:
        word += word[-1]  # Добавляем последний символ, если нечетное количество
    bigrams = [word[i:i + 2] for i in range(0, len(word), 2)]

    encrypted_bigrams = []
    for bigram in bigrams:
        encrypted_bigrams.append(encrypt_bigram(table, bigram))

    return "".join(encrypted_bigrams)


def encrypt_bigram(table, bigram):
    """
    Шифрует биграмму по правилам:
    - Если символы в одной строке -> заменяем на соседа справа.
    - Если в одном столбце -> заменяем на соседа снизу.
    - Если в разных строках и столбцах -> заменяем на символы противоположных углов прямоугольника.
    """
    n = len(table)
    char1, char2 = bigram[0], bigram[1]

    # Находим координаты символов в таблице
    pos1 = None
    pos2 = None
    for i in range(n):
        for j in range(n):
            if table[i][j] == char1:
                pos1 = (i, j)
            if table[i][j] == char2:
                pos2 = (i, j)

    if not pos1 or not pos2:
        raise ValueError(f"Символы {char1} или {char2} не найдены в таблице")

    i1, j1 = pos1
    i2, j2 = pos2

    # Правила шифрования
    if i1 == i2:  # Одна строка -> сосед справа
        new_j1 = (j1 + 1) % n
        new_j2 = (j2 + 1) % n
        encrypted_char1 = table[i1][new_j1]
        encrypted_char2 = table[i2][new_j2]
    elif j1 == j2:  # Один столбец -> сосед снизу
        new_i1 = (i1 + 1) % n
        new_i2 = (i2 + 1) % n
        encrypted_char1 = table[new_i1][j1]
        encrypted_char2 = table[new_i2][j2]
    else:  # Разные строки и столбцы -> противоположные углы
        encrypted_char1 = table[i1][j2]
        encrypted_char2 = table[i2][j1]

    return encrypted_char1 + encrypted_char2


def fixed(symbols, alphabet, target_num):
    """
    Дополняет список символов новыми символами из алфавита до достижения target_num (полного квадрата).

    :param symbols: Исходный список символов (например, ["М", "О", "С", "К", "В", "А"]).
    :param alphabet: Алфавит — набор символов для дополнения (например, "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ").
    :param target_num: Желаемое общее количество символов (должно быть полным квадратом, например, 9, 16, 25).
    :return: Дополненный список символов.
    """
    n = isqrt(target_num)
    if n * n != target_num:
        raise ValueError("target_num должно быть полным квадратом (например, 9, 16, 25)")

    # Убираем дубликаты в исходном списке
    unique_symbols = list(set(symbols))

    # Символы, которые нужно добавить (из алфавита, но не входящие в исходный список)
    available_symbols = [c for c in alphabet if c not in unique_symbols]
    needed = target_num - len(unique_symbols)

    if needed < 0:
        raise ValueError(
            f"Исходный список уже содержит {len(unique_symbols)} символов, что больше target_num={target_num}")
    if needed > len(available_symbols):
        raise ValueError(f"Не хватает символов в алфавите: нужно {needed}, доступно {len(available_symbols)}")

    # Добавляем случайные символы из алфавита
    new_symbols = random.sample(available_symbols, needed)
    result = unique_symbols + new_symbols

    # Перемешиваем результат, чтобы новые символы не были в конце
    random.shuffle(result)

    return result


# Пример использования:
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbols = list("Противоположность".upper())
print(len(symbols))

# Добавляем 3 символа (итого 9 = 3x3)
extended_symbols = fixed(symbols, alphabet, 25)
print("Дополненный список:", extended_symbols)



file_path, encrypted_word = generate_encrypted_table(extended_symbols, symbols, "encrypted_example.html")
print(f"HTML-таблица сохранена в файл: {file_path}")
print(f"Зашифрованное слово: {encrypted_word}")