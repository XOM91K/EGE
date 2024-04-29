for x in '0123456789abcdefg':
    for y in '0123456789abcdefg':
        c1 = int('7' + x + '589' + y, 17)
        c2 = int('EE' + x + y + '9AC', 17)
        if (c1 + c2) % 13 == 0:
            c1 = int('7' + x + '589' + '3', 17)
            c2 = int('EE' + x + '3' + '9AC', 17)
            print(x, (c1 + c2) // 13)