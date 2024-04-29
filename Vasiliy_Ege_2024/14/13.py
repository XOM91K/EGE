for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
        c = int('B' + y + x + '6R94E' + x, 30) + int('M' + y + 'KGN' + x, 30)
        if c % 10 == 0:
            print(x, y, c // 10)