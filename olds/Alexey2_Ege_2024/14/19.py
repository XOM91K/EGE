def dv(d):
    s = ''
    while d > 0:
        s += str(d %9)
        d //= 9
    return s[::-1]
d = 2 * 729 ** 2019 + 2 * 243**2020 - 81 **2021 + 2 * 27**2022 - 2 * 9**2023 - 2024
n = str(dv(d))
print(len(n) - n.count('0'))