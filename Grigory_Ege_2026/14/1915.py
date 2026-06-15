def v13(d):
    s = []
    while d > 0:
        s.append(str(d % 13))
        d //= 13
    return s[::-1]
for x in range(1, 5001):
    c = (7 * 13 ** 180 + 5 * 13 ** 120 - x)
    n = v13(c)
    if n.count('0') == 60:
        print(x)
