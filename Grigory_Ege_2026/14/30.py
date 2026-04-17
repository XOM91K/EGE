def v27(d):
    a = []
    while d > 0:
        a.append(d % 27)
        d //= 27
    return a[::-1]
d = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
d = v27(d)
d = len([y for y in d if y > 9])
print(d)