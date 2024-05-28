for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((120 <= x <= 130) <= (x % 7 != 0)) or (A > 2 * x)) == 0:
            can = False
    if can:
        print(A)