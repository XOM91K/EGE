k = 0
for Y in range(1, 101):
    for x in range(1, 25):
        c1 = 8 * 25 ** 6 + 10 * 25 ** 5 + 15 * 25 ** 4 + 7 * 25 ** 3 + x * 25 ** 2 + 1 * 25 + 1
        c2 = x * 25 ** 4 + 13 * 25 ** 3 + 10 * 25 ** 2 + 8 * 25 + 7
        if (c1 + c2) % Y == 0:
            print(Y)
            k += 1
            break
print(k)