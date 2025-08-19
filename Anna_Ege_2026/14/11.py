def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
d = 53 ** 123 + 65 ** 2222 - 172 ** 12
d = v7(d)
sm = 0
for x in range(1, 6):
    sm += d.count('6' + str(x))
print(sm)