def v19(d):
    ct = 0
    while d > 0:
        if d % 19 == 18:
            ct += 1
        d //= 19
    return ct
for x in range(1, 10000):
    c = 19 ** 270 + 19 ** 240 + 19 ** 190 + 19 ** 180 - x
    c = v19(c)
    if c == 177:
        print(x)