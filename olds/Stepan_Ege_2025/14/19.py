def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1, 3001):
    d = 9 ** 150 + 9 ** 30 - x
    d = v9(d)
    if d.count('0') == 122:
        print(x)