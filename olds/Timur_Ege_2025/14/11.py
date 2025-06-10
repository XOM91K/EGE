import string
print(string.ascii_uppercase)
for x in range(30):
    for y in range(30):
        c1 = 11 * 30 ** 8 + y * 30 ** 7 + x * 30 ** 6 + 6 * 30 ** 5 + 27 * 30 ** 4 + 9 * 30 ** 3 + 4 * 30 ** 2 + 14 * 30 ** 1 + x
        c2 = 22 * 30 ** 5 + y * 30 ** 4 + 20 * 30 ** 3 + 16 * 30 ** 2 + 23 * 30 ** 1 + x
        if (c1 + c2) % 10 == 0:
            print(x, y, (c1 + c2) // 10)