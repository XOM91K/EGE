def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1, 10000):
    c = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    c = v9(c)
    if abs(c.count('2') - c.count('8')) == 471:
        print(x)