for x in range(0, 23):
    d1 = 1 * 23 ** 7 + 1 * 23 ** 6 + 3 * 23 ** 5 + 5 * 23 ** 4 + 3 * 23 ** 3 + x * 23 ** 2 + 1 * 23 ** 1 + 2 * 23 ** 0
    d2 = 1 * 23 ** 5 + 3 * 23 ** 4 + 5 * 23 ** 3 + x * 23 ** 2 + 2 * 23 ** 1 + 1 * 23 ** 0
    if (d1 + d2) % 22 == 0:
        print((d1 + d2) // 22)