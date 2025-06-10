def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return F(n / 2)
ct = 0
# 45, 55, 65,
for x in range(1, 100000):
    if F(x) == 2:
        ct += 1
        print(x)
print(ct)