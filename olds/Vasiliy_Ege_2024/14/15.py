c = 3 * (2187 ** 2020) + 3 * (729 ** 2021) - 2 * (81 ** 2022) + (27**2023) - 4 * (3 ** 2024) - 2029
s = []
while c > 0:
    s.append(c % 27)
    c //= 27
ct = 0
for x in s:
    if x in range(10, 27):
        ct += 1
print(ct)