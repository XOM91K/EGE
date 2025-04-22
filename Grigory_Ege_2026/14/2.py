import string
print(string.ascii_uppercase)
for x in range(17):
    for y in range(17):
        c1 = 7 * 17 ** 5 + x * 17 ** 4 + 5 * 17 ** 3 + 8 * 17 ** 2 + 9 * 17 ** 1 + y
        c2 = 14 * 17 ** 6 + 14 * 17 ** 5 + x * 17 ** 4 + y * 17 ** 3 + 9 * 17 ** 2 + 10 * 17 ** 1 + 12
        if (c1 + c2) % 13 == 0:
                print(y, (c1 + c2) // 13)
# print(ord('А'))
# for x in range(1040, 1040 + 32):
#     print(chr(x), end='')