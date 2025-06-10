def F(n):
    if n >= 1000:
        return 1000
    elif n % 2 != 0:
        return n * F(n + 1)
    else:
        return n * F(n + 1) / 2
print(F(998) / F(1001))