F = [[]] * 10_000
for n in range(3000):
    if n == 1:
        F[n] = 1
    else:
        F[n] = (n - 1) * F[n - 1]

numerator = F[2024] + 2 * F[2023]
denuminator = F[2022]
result = numerator/denuminator
print(result)