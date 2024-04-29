for x in '0123456789abcdefg':
    c1 = int('10' + x + '0', 17)
    c2 = int('F0' + x + 'FF', 17)
    if (c1 + c2) % 13 == 0:
        print((c1 + c2) // 13)