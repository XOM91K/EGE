import string
print(string.ascii_uppercase)
for x in '012346789ABCDEFGHIJKLMNOPQRST':
    for y in '012346789ABCDEFGHIJKLMNOPQRST':
        c1 = int('B' + y + x + '6R94E' + x, 30)
        c2 = int('M' + y + 'KGN' + x, 30)
        if (c1 + c2) % 10 == 0:
            c1 = int('B' + '4' + x + '6R94E' + x, 30)
            c2 = int('M' + '4' + 'KGN' + x, 30)
            print(x, (c1 + c2) // 10)