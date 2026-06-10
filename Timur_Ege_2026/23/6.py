def g(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return g(x + 1, y) + g(x * 2, y) + g(x * 3, y)

print(g(6, 48))
print(g(6, 14) * g(14, 48))
print(g(6, 18) * g(18, 48))