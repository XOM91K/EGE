import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
        c1 = int(f'B{y+x}6r94e{x}', 30)
        c2 = int(f'M{y}KGN{x}', 30)
        if (c1 + c2) % 10 == 0:
            c1 = int(f'B4{x}6r94e{x}', 30)
            c2 = int(f'M4KGN{x}', 30)
            print(x, (c1 + c2) // 10)