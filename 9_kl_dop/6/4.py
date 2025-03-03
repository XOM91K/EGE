q = ((13, 2), [11, 12], (-12, 12), (2, -2), [-10, -10], (6, -5), (2, 8), (9, 10), (1, 13))
for A in range(-100, 100):
    ct = 0
    for s, t in q:
        if s > A or t > 12:
            ct += 1
        else:
            pass
    if ct == 7:
        print(A)