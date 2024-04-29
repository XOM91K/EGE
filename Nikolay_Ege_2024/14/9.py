def f(d, n):
    s = ''
    while d > 0:
        s += str(d % n)
        d //= n
    return s[::-1]
d = 123
for x in range(2, 11):
    print(d, f(d, x), x)
