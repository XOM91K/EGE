for x in range(44):
    c1 = 1 * 44 ** 3 + x * 44 ** 2 + 2 * 44 + 3
    c2 = 3 * 44 ** 3 + 2 * 44 ** 2 + x * 44 + 1
    if (c1 + c2) % 42 == 0:
        print((c1 + c2) // 42)