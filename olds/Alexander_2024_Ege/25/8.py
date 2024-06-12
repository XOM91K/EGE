def dels(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 7 == 0:
                l.append(x)
            if (n // x) % 7 == 0:
                l.append(n // x)
    return sorted(set(l))
k = 0
for x in range(100_000_000, 1_000_000_000):
    if len(dels(x)) == 15:
        print(x, dels(x)[-1])
        k += 1
    if k == 5:
        break
k = 0
print('---')
for x in range(1_000_000_000, 100_000_000, -1):
    if len(dels(x)) == 15:
        print(x, dels(x)[-1])
        k += 1
    if k == 5:
        break