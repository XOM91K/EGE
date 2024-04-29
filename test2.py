def dels(n):
    dl = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dl.append(x)
            dl.append(n // x)
    return sorted(dl)
print(dels(100_000_000_000_000))
#100_000_000 5 sec   3 sec