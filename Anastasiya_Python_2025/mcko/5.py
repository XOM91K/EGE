for x in range(12):
    c1 = 1 * 12 ** 4 + 5 * 12 ** 3 + 4 * 12 ** 2 + x * 12 + 3
    c2 = 1 * 12 ** 4 + x * 12 ** 3 + 3 * 12 ** 2 + 6 * 12 + 5
    if (c1 + c2) % 13 == 0:
        print((c1 + c2) // 13)