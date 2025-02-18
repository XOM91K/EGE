def F(n):
    if n < 10:
        return n
    if n >= 10:
        return F(n % 10) + F(n // 10)
for x in range(1000000, 10000000):
    if F(x) == 159:
        print(x)