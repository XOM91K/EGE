def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n - 1) + F(n - 2)
    if n > 2 and n % 2 == 0:
        return sum([F(i) for i in range(1, n)])
print(F(24))