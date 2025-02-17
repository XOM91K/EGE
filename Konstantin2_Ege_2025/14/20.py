for x in '0123456789abcdef':
    for y in '0123456789abcdef':
        c1 = int(f'27a{x}23',16)
        c2 = int(f'8{y}e5d2', 16)
        if (c1 + c2) % 5 == 0:
            print(int(x, 16)+int(y, 16))