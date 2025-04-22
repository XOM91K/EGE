import random
from math import isqrt
import os


def generate_html_square(symbols, filename="table.html"):
    """
    Генерирует HTML-таблицу с символами и сохраняет в файл.

    :param symbols: Список символов (длина должна быть полным квадратом).
    :param filename: Имя файла для сохранения (по умолчанию 'table.html').
    :return: Путь к сохранённому файлу.
    """
    n = isqrt(len(symbols))
    if n * n != len(symbols):
        raise ValueError("Количество символов должно быть полным квадратом числа")

    random.shuffle(symbols)  # Перемешиваем символы

    # Генерация HTML-кода
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Случайный квадрат</title>
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
    </style>
</head>
<body>
    <h2>Квадрат {n}×{n}</h2>
    <table>
        {"".join(
        f"<tr>{''.join(f'<td>{symbols[i * n + j]}</td>' for j in range(n))}</tr>"
        for i in range(n)
    )}
    </table>
</body>
</html>
    """

    # Сохранение в файл
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return os.path.abspath(filename)


# Пример использования:
symbols = ["А", "Ш", "С", "Ц", "Д", "Е", "Ё", "Ж", "З"]
file_path = generate_html_square(symbols, "random_square.html")
print(f"HTML-таблица сохранена в файл: {file_path}")