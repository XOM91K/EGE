for x in '0123456789abcde':
    d1 = int('67845' + x + '65', 15)
    d2 = int('1' + x + '23456', 15)
    if (d1 + d2) % 14 == 0:
        print((d1 + d2) // 14)