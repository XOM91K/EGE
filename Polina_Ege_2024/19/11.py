def f(s, p):
    if s <= 0 and (p == 2 or p == 4):
        return 1
    elif s > 0 and p == 4:
        return 0
    elif s <= 0:
        return 0
    if p % 2 != 0:
        if s % 2 != 0:
            return f(s - 2, p + 1) or f(s - 3, p + 1) or f((s - 1) // 2, p + 1)
        else:
            return f(s - 2, p + 1) or f(s - 3, p + 1) or f(s // 2, p + 1)
    else:
        if s % 2 != 0:
            return f(s - 2, p + 1) and f(s - 3, p + 1) and f((s - 1) // 2, p + 1)
        else:
            return f(s - 2, p + 1) and f(s - 3, p + 1) and f(s // 2, p + 1)
for x in range(1, 31):
    if f(x, 0):
        print(x)
#2
#10 11