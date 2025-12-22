def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for y in range(1, 1000):
    a = 5 ** 50 - y
    w = v5(a)
    if w.count('4') == 47:
        print(y)