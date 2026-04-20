n = 1200000
for A in range(n, n + 1):
    can = True
    for x in range(0, n + 1):
        for y in range(0, n + 1):
            if ((x * y < A) or (5 * x < y) or (486 <= x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)