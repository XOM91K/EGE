for x in '0123456789abcde':
    for y in '012345789abcdefg':
        c1 = int('123' + x + '5', 15)
        c2 = int('67' + y + '9', 17)
        if (c1 + c2) % 131 == 0:
            print(x, y, (c1 + c2) // 131)