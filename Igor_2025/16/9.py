f = [0] * 50_000_000
for n in range(len(f)):
    if n == 0:
        f[n] = 0
    elif n > 0 and n % 4 < 2:
        f[n] = f[n // 4] + n % 4
    else:
        f[n] = f[n // 4] + (n % 4) - 1
print(f)
