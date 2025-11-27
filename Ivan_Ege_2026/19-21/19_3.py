def g(s, p):
    if s >= 56 and p == 2:
        return 1
    elif s <  56 and p == 2:
        return 0
    elif s >= 56 and p < 2:
        return 0
    if p%2==0:
        return g(s+1, p+1) or g(s+2, p+1) or g(s*3 if s%3==0 else s-100, p+1)
    else:
        return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s * 3 if s % 3 == 0 else s - 100, p + 1)

for s in range(1, 56):
    if g(s, 0):
        print(s)