for x in '0123456789abc':
    c1 = int('8' + x + '121', 13)
    c2 = int('7' + x + '575', 13)
    if (c1 - c2) % 19 == 0:
        print(x, (c1 - c2) // 19)