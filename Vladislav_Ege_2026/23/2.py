def g(n, m):
    if n > m or n == 20 or n == 25:
        return 0
    elif n == m:
        return 1
    elif n < m:
        return g(n + 1, m) + g(n * 2, m) + g(n ** 2, m)
print(g(2, 15) * g(15, 35) * g(35, 50))