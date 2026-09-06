def v7 (d):
    s = ''
    while d > 0:
        s += str (d % 7)
        d //= 7
    return s[::-1]
c = 8 ** 1006 + 5 ** 1947 + 505
c = v7(c)
# 66622 = 18 - 4 = 14
# 3 - 2 = 1
print ((c.count('6') * 6 - c.count('2') * 2))