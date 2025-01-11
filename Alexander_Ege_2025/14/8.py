for x in '0123456789ABCDEFG':
    for y in '0123456789ABCDEFG':
        c1 = int('7' + x + '589' + y, 17)
        c2 = int('EE' + x + y + '9AC', 17)
        if (c1 + c2) % 13 == 0:
            if y == '3':
                print((c1 + c2) // 13)