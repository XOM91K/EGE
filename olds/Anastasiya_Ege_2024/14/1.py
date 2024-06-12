for x in range(1, 68):
    num1 = 3 * 81 ** 3 + x * 81 ** 2 + 2 * 81 + 1
    num2 = 1 * 67 ** 3 + 7 * 67 ** 2 + x * 67 + 4
    if (num1 + num2) % 35 == 0:
        print((num1 + num2) // 35)