def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1000):
    s = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    s = v9(s)
    if abs(s.count('2') - s.count('8')) == 471:
        print(x)