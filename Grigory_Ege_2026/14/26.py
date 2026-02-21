def v5(d):
    s = ''
    while d > 0 :
        s += str(d%5)
        d //= 5
    return s[::-1]
for x in range (1,4001):
    n = 5 ** 17 + 5**12 - x
    e = v5(n)
    if e.count('0') > 9:
        print(x, e.count('0'))