import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHI':
    c1 = int('78' + x + '79643', 19)
    c2 = int('25' + x + '43', 19)
    c3 = int('63' + x + '5', 37)
    if (c1 + c2 + c3) % 18 == 0:
        print((c1 + c2 + c3) // 18)