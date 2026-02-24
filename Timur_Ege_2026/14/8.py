def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
for x in range(1, 10000):
    c = 81 ** 20 - 9 ** x + 50
    c = v9(c)
    if sum(map(int, str(c))) == 138:
        print(x)