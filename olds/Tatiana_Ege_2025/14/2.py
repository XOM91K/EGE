for x in '0123456789ABCDEFG':
    for y in '0123456789ABCDEFG':
        c1 = int(f'7{x}589{y}', 17)
        c2 = int(f'eE{x}{y}9Ac', 17)
        if (c1 + c2) % 13 == 0:
            print(x, y, (c1 + c2) // 13)