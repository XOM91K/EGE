import string

print(string.ascii_uppercase)
for x in range(42):
    a = x + 9 * 42 + 6 * 42 ** 2 + 5 * 42 ** 3 + 19 * 42 ** 4
    b = 10 + 18 * 42 + x * 42 ** 2 + 1 * 42 ** 3
    if (a + b) % 155 == 0:
        print(x, (a + b) // 155)
