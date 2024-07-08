for x in range(5001, 50000):
    d = 7 ** 100 - x
    ct = 0
    while d > 0:
        if d % 7 == 0:
            ct += 1
        d //= 7
    if ct == 5:
        print(x)
