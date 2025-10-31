def g(s, p):
    if s<=17 and (p==2 or p == 4):
        return 1
    if s>17 and p==4:
        return 0
    if s<=17 and p<4:
        return 0

    if p%2!=0:
        return g(s-1, p+1) or g(s//3 if s % 3 == 0 else s - 2, p+1) or g(s//5 if s % 5 == 0 else s - 3, p+1)
    else:
        return g(s-1, p+1) and g(s//3 if s % 3 == 0 else s - 2, p+1) and g(s//5 if s % 5 == 0 else s - 3, p+1)

for S in range(17, 100):
    if g(S, 0):
        print(S)