for A in range(300):
    c = 1
    for x in range(300):
        for y in range(300):
            if ((x < A) or (y < A) or (x + 2 * y > 50)) == 0:
                c = 0
                break
    if c:
        print(A)