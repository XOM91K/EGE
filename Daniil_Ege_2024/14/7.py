d = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
ct = 0
while d > 0:
    if d % 25 == 0:
        ct += 1
    d //= 25
print(ct)