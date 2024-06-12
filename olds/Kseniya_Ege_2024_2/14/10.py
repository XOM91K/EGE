for x in range(0, 2000):
    d = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    s = s[::-1]
    if s.count('0') == 1891:
        print(x)
        break