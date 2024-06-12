def F(n):
    print(n)
    if n <= 1:
        return 0.5
    else:
        return (n + 1) * F(n - 1)
print(F(200) / F(198))