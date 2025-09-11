import string
print(string.ascii_uppercase)
alp = '0123456789ABCDEFGHIJKLMNOP'
for x in range(0, 34):
    c1 = 16 * 34 ** 5 + 25 * 34 ** 4 + 4 * 34 ** 3 + 5 * 34 ** 2 + x * 34 ** 1 + 2 * 34 ** 0
    c2 = 25 * 34 ** 2 + 7 * 34 ** 1 + x * 34 ** 0
    c3 = x * 34 ** 4 + 10 * 34 ** 3 + 18 * 34 ** 2 + 9 * 34 ** 1 + 8 * 34 ** 0
    if (c1 + c2 * c3) % 13 == 0:
        print((c1 + c2 * c3) // 13)