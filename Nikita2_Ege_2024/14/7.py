for x in '0123456789abcdefghijklmno':
    c1 = int('2' + x + x + '26129', 25)
    c2 = int('54' + x + x + x + '711', 25)
    if (c1 + c2) % 24 == 0:
        print((c1 + c2) // 24)