def v25(d):
    s = []
    while d > 0:
        s.append(str(d % 25))
        d //= 25
    return s
c = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
c = v25(c)
print(c.count('0'))