def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]


for x in range(100000):
    d = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    d = v9(d)
    if abs(d.count('2') - d.count('8')) == 471:
        print(x)