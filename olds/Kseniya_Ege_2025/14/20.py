def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s

for x in range(1, 480):
    c =9 ** 1942 + 9 * 6 ** 971 + 214 - x
    d = v9(c)
    if abs(d.count('2') - d.count('8')) == 471:
        print(x)