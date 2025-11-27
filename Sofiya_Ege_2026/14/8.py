for m in range(10, 100):
    c1 = 2 + 4 * m + 2 * m ** 2 + 4 * m ** 3 + 3 * m ** 4
    c2 = 3 + 6 * m + 2 * m ** 2 + 9 * m ** 3
    if (c1 + c2) % 7 == 0:
        print(m, (c1 + c2) // 7)