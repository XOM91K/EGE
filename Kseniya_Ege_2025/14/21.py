import string
print(string.ascii_uppercase)
for x in range(18):
    c1 = 1 * 18 ** 5 + 1 * 18 ** 4 + 17 * 18 ** 3 + x * 18 ** 2 + 5
    c2 = 3 * 18 ** 6 + 15 * 18 ** 5 + x * 18 ** 4 + 5 * 18 ** 3 + 4 * 18 ** 2 + x * 18 ** 1 + 8
    c3 = 16 * 18 ** 4 + x * 18 ** 3 + x * 18 ** 2 + x * 18 ** 1 + 9
    if (c1 + c2 + c3) % 14 == 0:
        print((c1 + c2 + c3) // 14)