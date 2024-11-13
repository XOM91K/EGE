for x in range(1, 150000):
    d = 3 ** 200 + 3 ** 10 - x
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    s = s[::-1]
    if s.count('2') >= 200:
        print(x)