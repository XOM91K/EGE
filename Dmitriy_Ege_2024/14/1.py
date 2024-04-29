for x in '0123456789abc':
    c1 = int('537' + x + '623', 13)
    c2 = int('6' + x + '35' + x + '2', 13)
    if (c1 - c2) % 3 == 0:
        print(x, c1 - c2)