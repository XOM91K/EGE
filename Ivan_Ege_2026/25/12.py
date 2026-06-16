def mn(d):
    l = []
    x = 2
    while x * x <= d:
        while d % x == 0:
            l.append(x)
            d //= x
        x += 1 if x == 2 else 2
    if d > 1:
        l.append(d)
    return l
for x in range(2_2026_2027, 10 ** 9):
    mnn = mn(x)
    if len(mnn) == 6:
        if len([d for d in mnn if str(d).count('2') == 1]) == 6:
            print(x, max(mnn))