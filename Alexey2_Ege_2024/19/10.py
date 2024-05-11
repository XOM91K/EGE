def g(s,p):
    if (p == 3) and s >= 135:
        return True
    if p == 3 and s < 135:
        return False
    if p < 3 and s >= 135:
        return False
    if p % 2 == 0:
        return g(s+5, p+1) or g(s*3, p+1)
    else:
        return g(s+5, p+1) and g(s*3, p+1)
for S in range(1,135):
    if g(S,0) == True:
        print(S)