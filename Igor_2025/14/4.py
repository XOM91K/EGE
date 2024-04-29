def v6(n):
    s = ''
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s
for x in range(1, 1000):
    g = v6(5 ** 2026 + 7 * 5 ** 1013 + 107 - x)
    if g.count('5') - 28 == g.count('0'):
        print(x)
        break