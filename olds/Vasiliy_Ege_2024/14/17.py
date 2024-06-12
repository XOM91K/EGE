def v25(n):
    s = []
    while n > 0:
        s.append(n % 25)
        n = n // 25
    return s[::-1]

f = 4 * (3125 ** 2019) + 3 * (625 ** 2020) - 2 * (125 ** 2021) + (25 ** 2022) - 4 * 5 * 2023 - 2024
f = v25(f)
ct = 0
for x in f:
    if x > 10:
        ct += 1
print(ct)