def g(s, p):
    if s <= 15 and (p == 2 or p == 4):
        return 1
    if s > 15 and p == 4:
        return 0
    if s <= 15 and p < 4:
        return 0
    if p % 2 == 0:
        t = [g(s - k, p + 1) for k in range(2, 10) if s % k == 0]
        if not t:
            s -= 1
            return all([g(s - k, p + 1) for k in range(2, 10) if s % k == 0])
        else:
            return all(t)
    else:
        t = [g(s - k, p + 1) for k in range(2, 10) if s % k == 0]
        if not t:
            s -= 1
            return any([g(s - k, p + 1) for k in range(2, 10) if s % k == 0])
        else:
            return any(t)
for S in range(16, 1000):
    if g(S, 0):
        print(S)