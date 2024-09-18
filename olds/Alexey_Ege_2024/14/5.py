for x in range(1, 100):
    d = 81 ** 20 - 9 ** x + 50
    sm = 0
    while d > 0:
        sm += d % 9
        d //= 9
    if sm == 138:
        print(x)