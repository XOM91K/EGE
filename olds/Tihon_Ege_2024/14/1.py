for x in '012345789abcde':
    c1 = int('82' + x + '19', 15)
    c2 = int('6' + x + '073', 15)
    if (c1 - c2) % 11 == 0:
        print(x, (c1 - c2) // 11)