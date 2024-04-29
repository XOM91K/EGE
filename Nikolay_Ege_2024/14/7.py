import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
        c1 = int('235' + x + '12', 30)
        c2 = int('42' + y + '33', 30)
        if (c1 + c2) % 29 == 0:
            print(int(x, 30) + int(y, 30), (c1 + c2) // (int(x, 30) + int(y, 30)))
