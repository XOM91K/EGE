def g(s, p):
    if s >= 88 and (p == 2 or p == 4):
        return True
    elif s <= 88 and p == 4:
        return False
    elif s >= 88:
        return False
    if p % 2 != 0:
        return g(s*3, p+1) or g(s + 4,p+1) or g(s+1, p+1)
    else:
        return g(s*3, p+1) and g(s + 4,p+1) and g(s+1, p+1)
for i in range(1, 87):
    if g(i,0):
        print(i)