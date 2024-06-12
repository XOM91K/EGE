for A in range(300):
    c = True
    for x in range(300):
        for y in range(300):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 0:
                c = False
                break
    if c:
        print(A)