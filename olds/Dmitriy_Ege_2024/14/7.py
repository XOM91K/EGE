import string
d = string.ascii_lowercase
print(d)
for x in '0123456789abcdefghijklm':
    if (int('7' + x + '38596', 23) + int('14' + x + '36', 23) + int('61' + x + '7', 23)) % 22 == 0:
        print((int('7' + x + '38596', 23) + int('14' + x + '36', 23) + int('61' + x + '7', 23)) // 22)