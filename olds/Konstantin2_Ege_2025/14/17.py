def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1, 1000):
    n = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    n = v9(n)
    if abs(n.count('2') - n.count('8')) == 471: #module  absolute
        print(x)