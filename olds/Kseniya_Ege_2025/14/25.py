import string

print(string.ascii_uppercase)
a = []
for x in range(1, 25):
    c1 = 8 * 25 ** 6 + 10 * 25 ** 5 + 15 * 25 ** 4 + 7 * 25 ** 3 + x * 25 ** 2 + 1 * 25 ** 1 + 1 * 25 ** 0
    c2 = x * 25 ** 4 + 13 * 25 ** 3 + 10 * 25 ** 2 + 8 * 25 ** 1 + 7 * 25 ** 0
    for y in range(1, 101):
        if (c1 + c2) % y == 0:
            a.append(y)
print(len(set(a)))