ENC = [
    182, 178, 184, 182, 130, 91, 132, 140, 91, 138, 162, 174, 166, 38, 128, 85,
    164, 93, 212, 242, 188, 83, 89, 115
]
def rol1(x):
    """Поворот влево на 1 бит (Rotate Left)"""
    return ((x >> 1) | (x << 7)) & 0xFF
MASK = 0x5A
d = []
for i, char in enumerate(ENC):
    # Этап 1: Смещение по позиции (добавляем индекс)
    final = char ^ MASK
    final = rol1(final)
    final = (final - i) & 0xFF
    d.append(final)
print(bytes(d))