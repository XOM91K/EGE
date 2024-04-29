d = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029


def v27(n):
    ost = []
    while n > 0:
        ost.append(n % 27)
        n //= 27
    return ost[::-1]
ct = 0
for x in range(10, 30):
    ct += v27(d).count(x)
print(ct)