d = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
s = []
while d > 0:
    s.append(d % 27)
    d //= 27
s = s[::-1]
ct = 0
for x in s:
    if x > 9:
        ct += 1
print(ct)