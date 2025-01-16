def g(s,p):
    if (p==4 or p ==2) and s>=39:
        return 1
    elif p==4 and s<39:
        return 0
    elif p<4 and s>=39:
        return 0
    if p%2==0:
        return g(s+1, p+1) and g(s+3, p+1) and g(s*2, p+1)
    else:
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
for S in range(1,39):
    if g(S,0):
        print(S)