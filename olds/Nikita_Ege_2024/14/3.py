for x in '0123456789abcdefg':
    if (int('12346' + x + '17', 17) + int('7' + x + '171', 17)) % 16 == 0:
        print((int('12346' + x + '17', 17) + int('7' + x + '171', 17)) // 16)