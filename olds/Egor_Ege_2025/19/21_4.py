def f(s, p):
    if s >= 82 and (p == 2 or p == 4):
        return 1
    if s < 82 and p == 4:
        return 0
    if s >= 82 and p < 4:
        return 0
    if p % 2 != 0:
        return f(s + 2, p + 1) or f(s + 4, p + 1) or f(s * 3, p + 1)
    else:
        return f(s + 2, p + 1) and f(s + 4, p + 1) and f(s * 3, p + 1)
for x in range(1, 82):
    if f(x, 0):
        print(x)