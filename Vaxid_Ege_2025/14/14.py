def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1, 1000):
    c = 81 ** 20 - 9 ** x + 50
    c = v9(c)
    if sum(map(int, c)) == 138:
        print(x)