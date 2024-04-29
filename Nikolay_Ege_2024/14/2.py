import string
print(string.ascii_uppercase)
for x in '0123456789abcdefghijkl':
    c1 = int('18' + x + '89957', 22)
    c2 = int('80' + x + '33', 22)
    c3 = int('521' + x + '6', 22)
    if (c1 + c2 + c3) % 21 == 0:
        print(x, (c1 + c2 + c3) // 21)