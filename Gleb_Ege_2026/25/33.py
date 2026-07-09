def dels(d):
    l = []
    x = 2
    while x * x <= d:
        while d % x == 0:
            l.append(x)
            d //= x
        x += 1
    if d > 1:
        l.append(d)
    return l
print(dels(2_000_000_125))