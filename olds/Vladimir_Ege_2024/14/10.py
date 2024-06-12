for x in '0123456789abcdef':
    if (int('10' + x + 'a', 16) + int('Ff' + x + '78', 16)) % 19 == 0:
        print(x, (int('10' + x + 'a', 16) + int('Ff' + x + '78', 16)) / 19)