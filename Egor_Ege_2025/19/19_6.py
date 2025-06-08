def f(s1, s2, p):
    if s1 + s2 >= 323 and (p == 2 or p == 4):
        return 1
    if s1 + s2 < 323 and p == 4:
        return 0
    if s1 + s2 >= 323 and p < 4:
        return 0
    if p % 2 != 0:
        return f(s1 +3,s2, p + 1) or f(s1 * 2,s2,  p + 1) or f(s1, s2 + 3, p + 1) or f(s1, s2 * 2, p + 1)
    else:
        return f(s1 +3,s2, p + 1) and f(s1 * 2,s2,  p + 1) and f(s1, s2 + 3, p + 1) and f(s1, s2 * 2, p + 1)

for x in range(1, 200):
    if f(123, x, 0):
        print(x)