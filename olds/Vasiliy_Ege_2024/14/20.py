d = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
ct = 0
while d > 0:
    if d % 27 > 9:
        ct += 1
    d //= 27
print(ct)