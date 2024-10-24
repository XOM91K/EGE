import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
        c1 = int('B' + y + x + '6R94E' + x, 30)
        c2 = int('M' + y + 'KGN' + x, 30)
        if (c1 + c2) % 10 == 0:
            print(x, y, (c1 + c2) // 10)