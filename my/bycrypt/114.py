# Скрипт для кодирования/декодирования флага "Sigma-Core"

# Прямые преобразования (как в основном скрипте)
def encode_transform(x, i):
    M = [5, 17, 23, 29, 41, 53, 61, 73, 83, 97, 101, 113, 127, 131, 149, 157]

    # Этап 1: Сложение с элементом из M
    a = (x + M[i % 16]) & 0xFF

    # Этап 2: Циклический сдвиг влево на 3 бита
    b = ((a << 3) | (a >> 5)) & 0xFF

    # Этап 3: Перестановка битов (swap pairs)
    # (x & 0xCC)>>2 | (x & 0x33)<<2
    # 0xCC = 11001100, 0x33 = 00110011
    # Меняет местами пары битов: биты 7-6 ↔ 5-4, биты 3-2 ↔ 1-0
    d = ((b & 0xCC) >> 2 | (b & 0x33) << 2) & 0xFF

    # Этап 4: XOR с динамической маской
    e = d ^ (0xA5 + (i * 13)) & 0xFF

    return e


# Обратные преобразования (для декодирования)
def decode_transform(enc_byte, i):
    M = [5, 17, 23, 29, 41, 53, 61, 73, 83, 97, 101, 113, 127, 131, 149, 157]

    # Обратный этап 4: XOR (обратно сам себе)
    d = enc_byte ^ (0xA5 + (i * 13)) & 0xFF

    # Обратный этап 3: Перестановка битов (обратно сам себе)
    b = ((d & 0xCC) >> 2 | (d & 0x33) << 2) & 0xFF

    # Обратный этап 2: Циклический сдвиг вправо на 3 бита
    a = ((b >> 3) | (b << 5)) & 0xFF

    # Обратный этап 1: Вычитание элемента из M
    x = (a - M[i % 16]) & 0xFF

    return x


# Флаг для задачи (l33t формат)
flag = "CTF{s1gm4_c0r3_1s_1mp3n3tr4bl3!}"
print(f"Оригинальный флаг: {flag}")
print(f"Длина: {len(flag)}")

# Кодируем флаг для получения массива V
encoded = []
for i, char in enumerate(flag):
    encoded.append(encode_transform(ord(char), i))

print(f"\nЗакодированный массив V:")
print(encoded)

# Декодируем обратно для проверки
decoded_chars = []
for i, enc_byte in enumerate(encoded):
    decoded_code = decode_transform(enc_byte, i)
    decoded_chars.append(chr(decoded_code))

decoded_flag = ''.join(decoded_chars)
print(f"\nДекодированный флаг: {decoded_flag}")
print(f"Совпадение: {flag == decoded_flag}")

# Код для участников CTF (решение)
print("\n" + "=" * 50)
print("РЕШЕНИЕ ДЛЯ УЧАСТНИКОВ CTF:")
print("=" * 50)
print("Чтобы получить флаг, нужно декодировать массив V:")

V = [202, 121, 215, 78, 229, 186, 243, 100, 142, 223, 108, 149, 254, 115, 160, 237, 122, 171, 244, 97, 138, 219, 106,
     151, 252, 117, 166, 231, 124, 177, 246, 103, 144, 211, 110]

print(f"V = {V}")
print("\nАлгоритм декодирования:")
print("1. Для каждого байта V[i]:")
print("   e = V[i] ^ (0xA5 + i*13)")
print("   d = ((e & 0xCC) >> 2 | (e & 0x33) << 2)")
print("   b = ((d >> 3) | (d << 5)) & 0xFF")
print("   a = (b - M[i % 16]) & 0xFF")
print("   где M = [5,17,23,29,41,53,61,73,83,97,101,113,127,131,149,157]")
print("\nПолученный флаг:", end=" ")

# Автоматически декодируем и показываем флаг
solution = []
for i, enc_byte in enumerate(V):
    decoded = decode_transform(enc_byte, i)
    solution.append(chr(decoded))

print(''.join(solution))