d = 2 * 729 ** 2019 + 2 * 243 ** 2020 - 81 ** 2021 + 2 * 27 ** 2022 - 2 * 9 ** 2023 - 2024
s = []
while d > 0:
    s.append(d % 9)
    d //= 9
print(len(s) - s.count(0))