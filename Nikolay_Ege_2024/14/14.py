def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
d = 2 * 729 ** 2019 + 2 * 243 ** 2020 - 81 ** 2021 + 2 * 27 ** 2022 - 2 * 9 ** 2023 - 2024
d = v9(d)
print(len(d) - d.count('0'))