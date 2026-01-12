def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
for x in range(1, 4001):
    d = v5(5**17 + 5**12 - x)
    if d[0] != 0 and d.count('0') > 9:
        print(x, d)