q = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
for A in range(-1000, 1000):
    ct = 0
    for s, t in q:
        if (s > 10) or (t > A):
            pass
        else:
            ct += 1
    if ct == 3:
        print(A)