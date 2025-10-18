def v6(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
for x in range(1, 10001):
    d = 6 ** 900 + 6 ** 10 - x
    d = v6(d)
    if d.count('3') == d.count('5'):
        print(x)