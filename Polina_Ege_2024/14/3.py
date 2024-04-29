for A in range(1, 100000):
    for x in '0123456789abc':
        for y in '0123456789abc':
            if (int('2' + y + '23' + x + '5', 15) + A) % int('67' + x + '9' + y, 13) == 0:
                print(A)
