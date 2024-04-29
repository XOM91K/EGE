for A in range(300):
    can = True
    for x in range(300):
        for y in range(300):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 0:
                can = False
    if can:
        print(A)