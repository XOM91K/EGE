for x in range(17):
    for y in range(17):
        c1 = 7 * 17 ** 5 + x * 17 ** 4 + 5 * 17 ** 3 + 8 * 17 ** 2 + 9 * 17 ** 1 + y * 17 ** 0
        c2 = 14 * 17 ** 6 + 14 * 17 ** 5 + x * 17 ** 4 + y * 17 ** 3 + 9 * 17 ** 2 + 10 * 17 ** 1 + 12 * 17 ** 0
        if (c1 + c2) % 13 == 0:
            if y == 3:
                print((c1 + c2) // 13)