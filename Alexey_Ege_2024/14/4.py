for x in range(4101, 8000):
    d = 3 ** 100 - x
    ct = 0
    while d > 0:
        if d % 3 == 0:
            ct += 1
        d //= 3
    if ct == 1:
        print(x)