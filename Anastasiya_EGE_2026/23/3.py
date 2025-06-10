def F(s, t):
    if s > t:
        return 0
    if s == t:
        return 1
    return F(s + 1, t) + F(s + 2, t) + F(s + 4, t)
print(F(4, 10) * F(10, 12) * F(12, 14))