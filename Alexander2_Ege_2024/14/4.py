def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s[::-1]
d = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
d = v27(d)
print(len(d) - d.count(0))
ct = 0