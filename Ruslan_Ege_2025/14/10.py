def f3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
for x in range(1, 100000):
    d = f3(3 ** 200 + 3 ** 10 - x)
    if d.count('2') == 200:
        print(x)