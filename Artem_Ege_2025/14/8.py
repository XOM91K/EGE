def v6(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
for x in range(1, 10001):
    a = 6 ** 900 + 6 ** 10 - x
    a = v6(a)
    if a.count('3') == a.count('5'):
        print(x)