d = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029


def v27(n):
    s = []
    while n > 0:
        s.append(n % 27)
        n //= 27
    return s[::-1]

g =v27(d)
ct = 0
for x in g:
    if x > 9:
      ct += 1
print(ct)
