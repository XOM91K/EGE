for x in '0123456789abcdefghigh':
    for y in '0123456789abcdefghigh':
        c1 = int('g2ba' + y + 'i' + x + x, 21)
        c2 = int('g' + x + '4' + y + 'dfi', 21)
        if (c1 + c2) % 7 == 0:
            c1 = int('g2ba6i' + x + x, 21)
            c2 = int('g' + x + '46dfi', 21)
            print((c1 + c2) // 7)