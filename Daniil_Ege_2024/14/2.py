import string
print(string.ascii_uppercase)
for x in '012346789abcdefgh':
    c1 = int('7' + x + '38596', 23)
    c2 = int('14' + x + '36', 23)
    c3 = int('61' + x + '7', 23)
    if (c1 + c2 + c3) % 22 == 0:
        print((c1 + c2 + c3) // 22)