ENC = [
        182, 178, 184, 182, 130, 91, 132, 140, 91, 138, 162, 174, 166, 38, 128, 85,
        164, 93, 212, 242, 188, 83, 89, 115
    ]
def rol1(x):
    """Поворот влево на 1 бит (Rotate Left)"""
    return ((x >> 1) | (x << 7)) & 0xFF
encrypted_input = []
for i, char in enumerate(ENC):
    # Этап 1: Смещение по позиции (добавляем индекс)
    x = char ^ 0x5A #(char - i) & 0xFF

    # Этап 2: Поворот ROL1
    y = rol1(x)

    # Этап 3: Применяем маску
    final = (y - i) & 0xFF #y ^ 0x5A

    encrypted_input.append(final)
print(bytes(encrypted_input))