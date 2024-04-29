for A in range(300):
    can = True
    for x in range(300):
        for y in range(300):
            if ((3 * y + 2 * x != 130) or (3 * x > A) or (2 * y > A)) == 0:
                can = False
    if can:
        print(A)