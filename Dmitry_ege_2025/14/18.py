import string
print(string.ascii_uppercase)
for x in range(22):
    c1 = 12 * 22 ** 1 + 10 * 22 ** 2 + x * 22 ** 3 + 3 * 22 ** 4 + 2 * 22 ** 5 + 10 * 22 ** 6
    c2 = 7 * 22 ** 1 + 6 * 22 ** 2 + 1 * 22 ** 3 + 2 * 22 ** 4 + x * 22 ** 5 + 11 * 22 ** 6 + 16 * 22 ** 7
    if (c1 + c2) % 21 == 0:
        print(((c1 + c2) // 22))