def F(n, k):
    k += 1
    if n > 1:
        F(n - 2, k + 1)
        F(n // 2, k + 1)
        k += 1
    k += 1
    return k
print(F(127, 0))