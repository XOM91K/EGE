for x in range(1, 10001):
    d = 6 ** 900 + 6 ** 10 - x
    s = []
    while d > 0:
        s.append(d % 6)
        d //= 6
    if s.count(3) == s.count(5):
        print(x)