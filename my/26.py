import struct

# --- Вставь сюда свои данные ---
rectangle_hex = (
    "950000005900000012000000220000003a000000730000007900000065000000580000004c000000"
    "2b0000006900000023000000210000000c0000007f00000036000000030000007a00000076000000"
    "220000002c0000006700000062000000230000002b00000026000000b2000000b100000050000000"
    "f10000009f000000360000006100000006000000010000004600000023000000090000000c000000"
    "a000000013000000dd000000ca00000029000000d70000005400000052000000f000000036000000"
)
diagonal_hex = (
    "a900000090000000aa00000040000000f600000055000000d2000000450000007d0000003b000000"
    "9d0000000400000065000000bc00000090000000c5000000c50000005c0000001400000058000000"
    "650000006e0000000b00000062000000c000000067000000be00000060000000"
)

# --- Функция для конвертации HEX в uint32 массив ---
def hex_to_uint32_array(hex_string):
    hex_string = hex_string.replace(" ", "").replace("\n", "")
    arr = []
    for i in range(0, len(hex_string), 8):
        chunk = hex_string[i:i+8]
        if len(chunk) < 8:
            break
        arr.append(struct.unpack("<I", bytes.fromhex(chunk))[0])
    return arr

rectangle_xores = hex_to_uint32_array(rectangle_hex)
diagonal_xores = hex_to_uint32_array(diagonal_hex)

# --- Инициализация canvas 31x31 ---
canvas = [[0]*31 for _ in range(31)]

# --- 1. Восстановление диагонали ---
for i in range(len(diagonal_xores)):
    # XOR-уравнение диагонали: canvas[i-1][i-1] ^ canvas[i][i] ^ canvas[i+1][i+1] == diagonal_xores[i]
    # Так как мы начинаем с нулей, можем просто взять младший байт
    canvas[i][i] = diagonal_xores[i] & 0xFF

# --- 2. Восстановление верхнего левого блока 2x3 ---
# Берём первые несколько блоков (достаточно для 18 символов флага)
flag_bytes = []
block_count = 18  # длина флага
for idx in range(block_count):
    y = idx // 6  # каждые 6 блоков идут по новой строке
    x = (idx % 6) * 3  # каждые 3 байта — новый блок
    # Берём 5 уже известных байт, восстанавливаем 6-й
    u1 = canvas[y][x] if canvas[y][x] != 0 else 0
    u2 = canvas[y][x+1] if canvas[y][x+1] != 0 else 0
    u3 = canvas[y][x+2] if canvas[y][x+2] != 0 else 0
    u4 = canvas[y+1][x] if canvas[y+1][x] != 0 else 0
    u5 = canvas[y+1][x+1] if canvas[y+1][x+1] != 0 else 0
    # Вычисляем u6
    u6 = rectangle_xores[idx] ^ u1 ^ u2 ^ u3 ^ u4 ^ u5
    canvas[y+1][x+2] = u6 & 0xFF
    # Добавляем в флаг
    flag_bytes.append(u1 & 0xFF)

# --- Последние байты флага ---
# Добавляем ещё последние 2 байта из последнего блока
flag_bytes.append(canvas[0][1] & 0xFF)
flag_bytes.append(canvas[0][2] & 0xFF)

# --- Конвертируем в строку ---
flag = ''.join(chr(b) for b in flag_bytes)
print("Восстановленный флаг:", flag)
