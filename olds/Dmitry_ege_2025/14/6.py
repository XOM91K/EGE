def v3(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]
for y in range(1, 100000):
    d = 3 ** 200 + 3 ** 10 - y
    d = v3(d)
    if d.count('2') == 200:
        print(y)