# Скрипт для генерации правильного ENC массива и проверки флага

def dynamic_mask(pos):
    return (0x3D ^ (pos * 7)) & 0xFF


def ror2(x):
    return ((x >> 2) | (x << 6)) & 0xFF


def swap_nibbles(x):
    return ((x & 0x0F) << 4) | ((x & 0xF0) >> 4)


def encode_char(char, i):
    DELTA_TABLE = [3, 7, 11, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    char_code = ord(char)

    delta = DELTA_TABLE[i % len(DELTA_TABLE)]
    a = (char_code + delta) & 0xFF
    b = swap_nibbles(a)
    c = ror2(b)
    final = c ^ dynamic_mask(i)

    return final


def decode_char(enc_byte, i):
    DELTA_TABLE = [3, 7, 11, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    # Обратное преобразование
    c = enc_byte ^ dynamic_mask(i)  # Обратный XOR
    b = ((c << 2) | (c >> 6)) & 0xFF  # rol2 (обратное ror2)
    a = swap_nibbles(b)  # swap_nibbles обратно само себе
    char_code = (a - DELTA_TABLE[i % len(DELTA_TABLE)]) & 0xFF

    return char_code


# Флаг для проверки
flag = "CTF{n3o_krYpt0n_XX_1s_unbr34k4bl3!}"
print(f"Исходный флаг: {flag}")
print(f"Длина флага: {len(flag)}")

# Кодируем флаг для получения ENC
enc = []
for i, char in enumerate(flag):
    enc.append(encode_char(char, i))

print(f"\nЗакодированный массив ENC:")
print(enc)

# Декодируем обратно для проверки
decoded_chars = []
for i, enc_byte in enumerate(enc):
    decoded_code = decode_char(enc_byte, i)
    decoded_chars.append(chr(decoded_code))

decoded_flag = ''.join(decoded_chars)
print(f"\nДекодированный флаг: {decoded_flag}")
print(f"Флаги совпадают: {flag == decoded_flag}")
# CTF{n3o_krYpt0n_XX_1s_unbr34k4bl3!}