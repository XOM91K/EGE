for x in range(9, 37):
    d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    s = []
    while d > 0:
        s.append(d % x)
        d //= x
    print(x, s.count(8))