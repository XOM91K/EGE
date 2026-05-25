def v25(d):
    s = []
    while d > 0:
        s.append(d%25)
        d //= 25
    return s[::-1]
c = 25**340 + 25**79 - 5**60
for x in range(1_000_000, 1, -1):
    d = c + x
    d = v25(d)
    if d.count(0) == 287:
        print(x)