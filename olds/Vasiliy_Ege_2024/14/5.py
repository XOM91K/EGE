for x in '0123456789ABCDE':
    c1 = int('123' + x + '5', 15)
    c2 = int('1' + x + '233', 15)
    if (c1 + c2) % 14 == 0:
        print((c1 + c2) // 14)