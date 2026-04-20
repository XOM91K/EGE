n = 1_101_000
for A in range(n, 10 ** 10):
    can = True
    for x in range(5000):
        for y in range(5000):
            if ((x * y < A) or (5 * x < y) or (486 <= x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A, 'подходит')
        break
    else:
        print(A, 'не подходит')
        break