import string
print(string.ascii_lowercase)
for x in '0123456789abcdefghijklm':
    for y in '0123456789abcdefghijklm':
        c1 = int('9IE3' + y + x, 23)
        c2 = int('J5' + y + 'B' + x + 'L1', 23)
        if (c1 + c2) % 13 == 0:
            c1 = int('9IE3' + '3' + x, 23)
            c2 = int('J5' + '3' + 'B' + x + 'L1', 23)
            print(x, (c1 + c2) // 13)