for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 0:
                ok = False
                break
    if ok:
        print(A)
