def F(x, A):
    return ((x % 12 == 0) and (70 <= x <= 80) and (x % A != 0))


ct = 0
for A in range(1, 1000):
    if all([not F(x, A) for x in range(1, 1000)]):
        ct += 1
print(ct)
