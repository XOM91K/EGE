def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for x in range(70000, 10, -1):
    c = 5 ** 2025 + 5 ** 400 - x
    c = v5(c)
    if c.count('4') > 500:
        print(x)