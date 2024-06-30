for x in range(8301, 10000):
    d = 5 ** 100 - x
    ct = 0
    while d > 0:
        if d % 5 == 0:
            ct += 1
        d //= 5
    if ct == 4:
        print(x)