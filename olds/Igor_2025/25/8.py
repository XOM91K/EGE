def mn(n):
    dels = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dels.append(x)
            dels.append(n // x)
    dels = sorted(dels)
    return [dels[-1], dels[-2]]
for N in range(110_250_000, 110_300_000):
