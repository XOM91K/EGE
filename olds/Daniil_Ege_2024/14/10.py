for x in range(0, 31):
    a = 5 * 31 ** 4 + 1 * 31 ** 3 + x * 31 ** 2 + 2 * 31 ** 1 + 11 * 31 ** 0
    b = 3 * 31 ** 6 + 12 * 31 ** 5 + 14 * 31 ** 4 + x * 31 ** 3 + 3 * 31 ** 2 + 2 * 31 ** 1 + 1 * 31 ** 0
    if (a + b) % 17 == 0:
        print((a + b) // 17)
