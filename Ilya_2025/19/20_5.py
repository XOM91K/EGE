def f(n, p):
    if p == 3 and n >= 39:
        return 1
    elif p < 3 and n >= 39:
        return 0
    elif p == 3 and n < 39:
        return 0
    if p % 2 == 0:
        return f(n * 2, p + 1) or f(n + 1, p + 1) or f(n + 3, p + 1)
    else:
        return f(n * 2, p + 1) and f(n + 1, p + 1) and f(n + 3, p + 1)


for S in range(1, 39):
    if f(S, 0) == 1:
        print(S)
