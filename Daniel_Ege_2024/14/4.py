for x in '0123456789abcdefg':
    sl1 = int('12346' + x + '17', 17)
    sl2 = int('7' + x + '171', 17)
    if (sl1 + sl2) % 16 == 0:
        print((sl1 + sl2) / 16)