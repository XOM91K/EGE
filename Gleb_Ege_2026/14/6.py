def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for x in range(1, 100000):
    n = 3 ** 200 + 3 ** 10 - x
    n = v3(n)
    if n.count('2') == 200:
        print(x)