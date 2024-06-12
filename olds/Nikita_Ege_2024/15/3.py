for A in range(1000):
    c = 1
    for x in range(1000):
        for y in range(1000):
            if ((x < A) or (y < A) or (x + 2 * y) > 50) == 0:
                c = 0
    if c:
        print(A)
        break