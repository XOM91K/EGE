d = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024
ct = 0
while d > 0:
    if d % 27 > 9:
        ct += 1
    d //= 27
print(ct)