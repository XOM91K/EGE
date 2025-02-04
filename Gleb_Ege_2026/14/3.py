import string
print(string.ascii_uppercase)

for x in range(19):
    c1 = 10 * 19 ** 4 + 3 * 19 ** 3 + x * 19 ** 2 + 7 * 19 ** 1 + 4 * 19 ** 0
    c2 = x * 19 ** 5 + 4 * 19 ** 4 + 0 * 19 ** 3 + 8 * 19 ** 2 + 4 * 19 ** 1 + 6 * 19 ** 0
    if (c1 + c2) % 9 == 0:
        print(x, (c1 + c2) // 9)