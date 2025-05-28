for x in range (95):
    for y in range (95):
        n1 = 1 *95 ** 4 + x * 95 **3 + y * 95 **2 + x * 95 +5
        n2 = 6 * 95**4 + y * 95**3 + x * 95**2 + 1 * 95 + 7
        if (n1+n2) % 4221 == 0:
                print(x, y, hex((n1+n2) // 4221))