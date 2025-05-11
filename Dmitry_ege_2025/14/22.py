def v5(x):
    s = ''
    while x > 0:
        s += str(x % 5)
        x //= 5
    return s[::-1]
for y in range(1, 1000):
    d = 5 ** 50 - y
    d = v5(d)
    if d.count('4') == 47:
        print(y)