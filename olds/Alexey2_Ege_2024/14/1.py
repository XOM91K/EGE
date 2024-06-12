def v9(n):
    l = []
    while n > 0:
        l.append(n % 25)
        n //= 25
    return l[::-1]
d = 13 * 625 ** 1320 + 12 * 125 ** 1230 - 14 * 25 ** 1140 - 13 * 5 ** 1050 - 2500
print(v9(d).count(0))