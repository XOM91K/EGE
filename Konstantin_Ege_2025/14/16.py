for x in range(9, 100):
    d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    s = []
    while d > 0:
        s.append(d % x)
        d //= x
    print(s.count(8))
