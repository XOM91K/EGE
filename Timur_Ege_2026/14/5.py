def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
for x in range(1, 1000):
    c = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    c = v9(c)
    if c.count('2') - c.count('8') == 471 or c.count('8') - c.count('2') == 471:
        print(x)
