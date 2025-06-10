import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
        c1 = int(f'B{y}{x}6r94E{x}', 30)
        c2 = int(f'm{y}KgN{x}', 30)
        if (c1 + c2) % 10 == 0:
            print((c1 + c2) // 10, x, y)