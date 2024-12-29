def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
n = 53 ** 123 + 65 ** 2222 - 172 ** 12
n = v7(n)
sm = 0
for x in '12345':
    sm += n.count('6' + x)
print(sm)