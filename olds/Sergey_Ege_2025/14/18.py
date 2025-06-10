for x in range(1, 2031):
    d = 7 ** 170 + 7 ** 100 - x
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    if s.count('0') == 71:
        print(x)
