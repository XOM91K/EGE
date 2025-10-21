def fn(s, p):
    if s >= 68 and p == 3:
        return 1
    elif s < 68 and p == 3:
        return 0
    elif s >= 68 and p < 3:
        return 0

    if p % 2 == 0:
        return fn(s + 1, p + 1) or fn(s + 4, p + 1) or fn(s * 5, p + 1)
    else:
        return fn(s + 1, p + 1) and fn(s + 4, p + 1) and fn(s * 5, p + 1)
for S in range(1, 68):
    if fn(S, 0) == 1:
        print(S)