# Система диагностики потоков данных БАЙТ-77
# Детектор помех в передаче
# ВНИМАНИЕ: Обнаружена помеха в байт-потоке

def main():
    # Ключ подавления помех
    KEY = 0x2E

    # Поврежденные данные с помехами
    ENC = [
        88, 93, 65, 93, 70, 85, 86, 30, 92, 113, 31, 76, 87, 90, 29, 113, 88, 29, 113, 66, 31, 90, 83
    ]

    print("Система диагностики БАЙТ-77")
    print("Введите восстановленные данные:")

    try:
        user_input = input().strip()
    except EOFError:
        return

    # Корректируем помехи в байт-потоке
    # Применяем ключ подавления помех
    decrypted = ""
    for encrypted_byte in ENC:
        # Убираем помеху через XOR
        decrypted_char = chr(encrypted_byte ^ KEY)
        decrypted += decrypted_char
    print(decrypted)
    if user_input == decrypted:
        print("ДОСТУП РАЗРЕШЕН")
        print("ПОМЕХИ УСТРАНЕНЫ")
        print("БАЙТ-77: Поток данных восстановлен")
    else:
        print("ОШИБКА: Данные некорректны!")
        print("ДОСТУП ЗАПРЕЩЕН")


if __name__ == "__main__":
    main()