for x in '0123456789abcdefg':
    for y in '0123456789abcdefg':
        c1 = int('7' + x + '589' + y, 17)
        c2 = int('ee' + x + y + '9ac', 17)
        if (c1 + c2) % 13 == 0:
            c1 = int('7' + x + '5893', 17)
            c2 = int('ee' + x + '39ac', 17)
            print(x, (c1 + c2) // 13)