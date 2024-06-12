def F(n):
    return G(n - 1)
def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n - 2) + 1
ct = 0
for n in range(1, 101):
    if F(n) in [1, 4, 9, 16, 25, 36, 49]:
        ct += 1
print(ct)