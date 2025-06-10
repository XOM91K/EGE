for x in range(9,100):
    e = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    b = []
    while e > 0:
        b.append(e%x)
        e //= x
    print(b.count(8))