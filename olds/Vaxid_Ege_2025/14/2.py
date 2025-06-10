import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQ':
    c1 = int('3616465' + x, 27)
    c2 = int('99' + x + '95' + x + '69', 27)
    if (c1 + c2) % 26 == 0:
        print((c1 + c2) // 26)