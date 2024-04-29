for x in range(95):
    for y in range(95):
        d1 = 1 * 95 ** 4 + x * 95 ** 3 + y * 95 ** 2 + x * 95 + 5
        d2 = 6 * 95 ** 4 + y * 95 ** 3 + x * 95 ** 2 + 1 * 95 + 7
        if (d1 + d2) % 4221 == 0:
            print(hex((d1 + d2) // 4221), x,y)