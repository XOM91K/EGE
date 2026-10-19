def main():
    MASK = 0x5A
    ENC = [
        182, 178, 184, 182, 130, 91, 132, 140, 91, 138, 162, 174, 166, 38, 128, 85,
        164, 93, 212, 242, 188, 83, 89, 115
    ]

    print("Генератор ключей Конвейер-DE")
    print("Введите корректный ключ:")

    try:
        user_input = input().strip()
    except EOFError:
        return

    if len(user_input) != len(ENC):
        print("ОШИБКА: Неверная длина ключа!")
        print("СИСТЕМА ЗАБЛОКИРОВАНА")
        return

    def rol1(x):
        """Поворот влево на 1 бит (Rotate Left)"""
        return ((x << 1) | (x >> 7)) & 0xFF

    # Применяем трехступенчатый процесс конвейера к пользовательскому вводу
    encrypted_input = []
    for i, char in enumerate(user_input):
        # Этап 1: Смещение по позиции (добавляем индекс)
        x = (ord(char) + i) & 0xFF

        # Этап 2: Поворот ROL1
        y = rol1(x)

        # Этап 3: Применяем маску
        final = y ^ MASK

        encrypted_input.append(final)

    # Сравниваем зашифрованный ввод с эталоном
    if encrypted_input == ENC:
        print("ДОСТУП РАЗРЕШЕН")
        print("КОНВЕЙЕР ВОССТАНОВЛЕН")
        print("Конвейер-DE: Ключ сгенерирован успешно")
    else:
        print("ОШИБКА: Неверный ключ!")
        print("ДОСТУП ЗАПРЕЩЕН")


if __name__ == "__main__":
    main()