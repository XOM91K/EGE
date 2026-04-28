for A in range(1, 100):
    xy = [(6, 8), (3, 5), (-7, 2), (7, 7), (9, 8), (-1, 3), (-4, 5), (6, 9), (2, -1)]
    ct = 0
    for x, y in xy:
        if x > y and y > 0 and x > A:
            ct += 1
    if ct == 0:
        print(A)