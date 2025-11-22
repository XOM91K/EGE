# Загрузим файл и прочитаем его
with open('message.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Позиции символов (указаны в задании, но нумерация может быть с 0 или с 1)
positions = [1, 2, 3, 4, 13, 37, 55, 61, 98, 103, 146, 152, 154, 206, 254, 482, 527, 562, 581, 603]

# Попробуем оба варианта нумерации (с 0 и с 1)
result_0based = ''.join(text[pos] for pos in positions)
result_1based = ''.join(text[pos-1] for pos in positions)

print("Нумерация с 0:", result_0based)
print("Нумерация с 1:", result_1based)