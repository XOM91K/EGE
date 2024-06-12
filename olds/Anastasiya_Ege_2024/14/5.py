import string
alp = string.ascii_uppercase
print(alp)
cc = 0
for x in range(0, 1000):
    c = True
    for y in range(0, 1000):
        num1 = 5 * 20 ** 8 + y * 20 ** 7 + 4 * 20 ** 6 + x * 20 ** 5 + y * 20 ** 4 + 4 * 20 ** 3 + 17 * 20 ** 2 + 19 * 20 + 4
        num2 = 4 * 20 ** 6 + y * 20 ** 5 + 6 * 20 ** 4 + 11 * 20 ** 3 + y * 20 ** 2 + x * 20 + 1
        if (num1 + num2) % 15 != 0:
            c = False
    if c == True:
        num1 = 5 * 20 ** 8 + 8 * 20 ** 7 + 4 * 20 ** 6 + x * 20 ** 5 + 8 * 20 ** 4 + 4 * 20 ** 3 + 17 * 20 ** 2 + 19 * 20 + 4
        num2 = 4 * 20 ** 6 + 8 * 20 ** 5 + 6 * 20 ** 4 + 11 * 20 ** 3 + 8 * 20 ** 2 + x * 20 + 1
        print(x, num1 + num2)