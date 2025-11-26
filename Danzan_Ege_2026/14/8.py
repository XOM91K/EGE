def v25(d):
    s = []
    while d > 0:
        s.append(d % 25)
        d //= 25
    return s[::-1]
d = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
d = v25(d)
print(d.count(0))