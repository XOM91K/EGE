def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
for x in range(1, 10000):
    d = 81**20 - 9**x + 50
    d = v9(d)
    if sum(map(int, d)) == 138:
        print(x)