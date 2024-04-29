for n in range(1, 100):
    sm = 21 + 22 + 4 * n
    if sm % n == 0:
        print(n, sm)