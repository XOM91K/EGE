for X in range(1, 1000):
    d = 5 ** 2026 + 7 * 5 ** 1013 + 107 - X
    s = []
    while d > 0:
        s.append(d % 6)
        d //= 6
    if s.count(5) - s.count(0) == 28:
        print(X, s.count(5), s.count(0))
        break