def xor_decrypt(data, key):
    """Расшифровка данных с помощью XOR с заданным ключом"""
    return bytes([b ^ key for b in data])


def is_printable(text):
    """Проверяет, состоит ли текст только из печатных ASCII символов"""
    return all(32 <= byte <= 126 or byte in [9, 10, 13] for byte in text)


def main():
    # Читаем зашифрованный файл
    with open('flag.enc', 'rb') as f:
        encrypted_data = f.read()

    print(f"Размер зашифрованных данных: {len(encrypted_data)} байт")
    print(f"Первые 20 байт: {encrypted_data[:20]}")

    # Пробуем все возможные ключи (0-255)
    possible_flags = []

    for key in range(256):
        decrypted = xor_decrypt(encrypted_data, key)

        # Проверяем, похоже ли это на текстовый флаг
        if is_printable(decrypted):
            try:
                decoded_text = decrypted.decode('utf-8')
                # Ищем типичные форматы флагов
                if any(flag_marker in decoded_text for flag_marker in ['flag{', 'CTF{', 'FLAG{']):
                    print(f"🎉 ВОЗМОЖНЫЙ ФЛАГ с ключом {key}: {decoded_text}")
                    possible_flags.append((key, decoded_text))
                elif len(decoded_text) > 10:  # Просто покажем все читаемые результаты
                    print(f"Ключ {key:3d}: {decoded_text[:50]}...")
            except UnicodeDecodeError:
                # Пропускаем некорректные UTF-8 последовательности
                pass

    # Выводим все возможные флаги
    print("\n" + "=" * 50)
    print("ВОЗМОЖНЫЕ ФЛАГИ:")
    for key, flag in possible_flags:
        print(f"Ключ {key}: {flag}")

    # Если не нашли явных флагов, покажем все читаемые варианты
    if not possible_flags:
        print("Не найдено явных флагов. Попробуем все читаемые варианты:")
        for key in range(256):
            decrypted = xor_decrypt(encrypted_data, key)
            if is_printable(decrypted):
                try:
                    decoded_text = decrypted.decode('utf-8')
                    print(f"Ключ {key:3d}: {decoded_text}")
                except:
                    pass


if __name__ == "__main__":
    main()