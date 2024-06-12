def g(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return g(x + 1, y) + g(x * 2, y) + g(x * 3, y)
ct = 0
for x in range(2, 16):
    if x % 2 == 0:
        print(g(x, 15), x)
        ct += g(x, 15)

print(ct)