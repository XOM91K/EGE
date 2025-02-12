def g(s, p):
    if s <= 19 and p == 1:
        return 1
    if s > 19 and p == 1:
        return 0
    if s <= 19 and p < 1:
        return 0
    if p % 2 != 0:
        if s % 2 == 0 and s % 3 == 0:
            return g(s - 5, p + 1) and g(s // 2, p + 1) and g(s // 3, p + 1)
        elif s % 2 == 0:
            return g(s - 5, p + 1) and g(s // 2, p + 1)
        elif s % 3 == 0:
            return g(s - 5, p + 1) and g(s // 3, p + 1)
        else:
            return g(s - 5, p + 1) and g(s + 1, p + 1)
    else:
        if s % 2 == 0 and s % 3 == 0:
            return g(s - 5, p + 1) or g(s // 2, p + 1) or g(s // 3, p + 1)
        elif s % 2 == 0:
            return g(s - 5, p + 1) or g(s // 2, p + 1)
        elif s % 3 == 0:
            return g(s - 5, p + 1) or g(s // 3, p + 1)
        else:
            return g(s - 5, p + 1) or g(s + 1, p + 1)
A = {132, 141, 30, 159, 34, 36, 40, 168, 42, 43, 46, 49, 50, 52, 55, 58, 61, 62, 70, 74, 75, 82, 87, 88, 93, 94, 105, 106, 111, 112, 123}
B = {20, 21, 22, 23, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 42, 45, 48, 51, 54, 57}
for S in range(20, 1000):
    if g(S, 0):
        B.add(S)
print(B)
print(sorted(A.difference(B)))
#25
#30 34 или 43 49
#59