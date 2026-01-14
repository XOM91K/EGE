def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
g = []
for x in range(2, 1000):
    if is_prime(x):
        for y in range(2, 50):
            if 700_000 <= x ** y <= 1_000_000:
                g.append([x ** y, x])
for x in sorted(g):
    print(*x)
# [703921, 839], [704969, 89], [707281, 29], [823543, 7], [912673, 97]