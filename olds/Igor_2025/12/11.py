for n in range(1, 10000):
    d = 10 * 28 + 11 * 14 + 6 * n
    if d > 1000 and d % 20 == 0:
        print(n)
        break