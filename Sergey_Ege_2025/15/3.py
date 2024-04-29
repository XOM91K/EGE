for A in range(200):
    k = 0
    for x in range(200):
        for y in range(200):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 1:
                k += 1
    if k == 200 * 200:
        print(A)