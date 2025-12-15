for A in range(17000, 1, -1):
    can = True
    for x in range(1, 10000):
        for y in range(1, 10000):
            if ((x * y < A) or (x < 7 * y) or (343 < x)) == 0:
                can = False
                break
        if can == False:
            break
    print(A)
    if can:
        print(A, 'otv')