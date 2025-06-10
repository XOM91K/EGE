def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for x in range(1, 100000):
    d = 3 ** 200 + 3 ** 10 - x
    d = v3(d)
    if d.count('2') == 200:
        print(x)
