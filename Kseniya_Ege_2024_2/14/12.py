def per(n):
    ost = ''
    while n > 0:
        ost = ost + str(n % 19)
        n = n // 19
    return ost[::-1]

d = 2 * 729 ** 2019 + 2 * 243 ** 2020 - 81 ** 2021 + 2 * 27 ** 2022 - 2 * 9 ** 2023 - 2024
d = per(d)
print(len(d) - d.count('0'))