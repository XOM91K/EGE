for x in range(0, 100):
    d = 81 ** 20 - 9 ** x + 50
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    if sum(map(int, s)) == 138:
        print(x)