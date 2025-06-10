def g(s, p):
    if s <= 17 and p == 3:
        return True
    elif s > 17 and p == 3:
        return False
    elif s <= 17 and p < 3:
        return False
    if p % 2 != 0:
        return g(s - 1, p + 1) and g(s // 3 if s % 3 == 0 else s - 2, p + 1) and g(s // 5 if s % 5 == 0 else s - 3, p + 1)
    else:
        return g(s - 1, p + 1) or g(s // 3 if s % 3 == 0 else s - 2, p + 1) or g(s // 5 if s % 5 == 0 else s - 3, p + 1)
for S in range(18, 100):
    if g(S, 0):
        print(S)
#22
#23 66