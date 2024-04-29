for A in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 1:
                k += 1
    if k == 300 * 300:
        print(A)