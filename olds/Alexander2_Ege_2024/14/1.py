import string
print(string.ascii_lowercase)
for x in '0123456789abcdefghijklm':
    c1 = int(f'7{x}38596', 23)
    c2 = int(f'14{x}36', 23)
    c3 = int(f'61{x}7', 23)
    if (c1 + c2 + c3) % 22 == 0:
        print((c1 + c2 + c3) // 22)
