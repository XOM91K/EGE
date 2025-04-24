def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for x in range(1, 3000):
    c = 4 ** 210 + 4 ** 10 - x
    c = v4(c)
    if c.count('0') > 204:
        print(x, c.count('0'))