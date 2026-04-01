n = 100000
for A in range(n, 200_000):
    can = True
    for x in range(1, 100_000):
        for y in range(1, 100_000):
            if (((y < A) and (x < A)) or (89241 < 5 * y + x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)