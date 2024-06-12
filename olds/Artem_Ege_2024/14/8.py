for x in '0123456789abcdefg':
    for y in '0123456789abcdefg':
        s1 = int('7' + x + '589' + y, 17)
        s2 = int('EE' + x + y + '9ac', 17)
        if (s1 + s2) % 13 == 0:
            s1 = int('7' + x + '589' + '3', 17)
            s2 = int('EE' + x + '39ac', 17)
            print(x, (s1 + s2) // 13)