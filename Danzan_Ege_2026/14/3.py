import string
print(string.printable)
for x in '0123456789abcdefghijklmnopqrst':
    for y in '0123456789abcdefghijklmnopqrst':
        c1 = int(f'b{y}{x}6r94e{x}', 30)
        c2 = int(f'm{y}kgn{x}', 30)
        if (c1 + c2) % 10 == 0:
            print(x, y, (c1 + c2) // 10)