for A in range(1, 300):
    k = True
    for x in range(1, 300):
        for y in range(1, 300):
            if ((x < A) or (y < A) or (x + 2*y > 50)) == 0:
                k = False
    if k:
        print(A)