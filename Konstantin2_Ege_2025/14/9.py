for x in '0123456789abcdefg':
    for y in '0123456789abcdefg':
        c1 = int(f'7{x}589{y}',17)
        c2 = int(f'ee{x}{y}9ac', 17)
        if (c1 + c2) % 13 == 0:
            if y == '3':
                print((c1 + c2) // 13, x)