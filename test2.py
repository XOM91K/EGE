# password = input()
# if 16 < len(password) < 32:
#   if password[::3][::2][::1][::-1] == 'dec':
#     if password[::-1][::1][::2][::3] == '627':
#       if password[1] == password[2] == password[-2] == password[-1]:
#         if password[-3:-7:-1] == '0bfd':
#           if password[3:7:1] == '347e':
#             if password[7:11:1] == password[-11:-7:1] == '0ef4':
#               if sum([ord(x) for x in password]) == 1275:
#                 print('пароль верный')
#                 # aXXodsh 0ef4 hdXX
import random
import base64

XOR_KEY = random.randint(0, 255)

flag = "vsosh{asdadsad}"

encrypted_flag = []
for c in flag:
    encrypted_flag.append(ord(c) ^ XOR_KEY)

encrypted_flag = " ".join(map(str, encrypted_flag))
encrypted_flag = base64.b32encode(encrypted_flag.encode("utf-8")).decode("utf-8")
encrypted_flag = base64.b64encode(encrypted_flag.encode("utf-8")).decode("utf-8")

with open("encrypted_flag.txt", "w") as f:
    f.write(str(encrypted_flag))

