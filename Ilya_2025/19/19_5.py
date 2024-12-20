def f(n, p):
    if p==2 and n>=82:
        return 1
    elif p==2 and n<82:
        return 0
    elif p<2 and n>=82:
        return 0
    if p % 2 == 0:
        return f(n * 3, p + 1) or f(n + 2, p + 1) or f(n + 4, p + 1)
    else:
        return f(n * 3, p + 1) or f(n + 2, p + 1) or f(n + 4, p + 1)
for S in range(1,82):
    if f(S,0):
        print(S)