print('№19')
def g(s,p):
    if p==2 and s<=12:
        return 1
    elif p==2 and s>12:
        return 0
    elif p<2 and s<=12:
        return 0
    if p%2 !=0:
        return g(s-1,p+1) or g(s-2,p+1) or g(s-3,p+1) or g(s-4,p+1) or g(s-5,p+1) or g(s//5,p+1)
    else:
        return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1) and g(s - 4, p + 1) and g(s - 5, p + 1) and g(s // 5,p + 1)
for S in range(20,100):
    if g(S,0):
        print(S)


print('№20')
def g(s,p):
    if p==3 and s<=12:
        return 1
    elif p==3 and s>12:
        return 0
    elif p<3 and s<=12:
        return 0
    if p%2 ==0:
        return g(s-1,p+1) or g(s-2,p+1) or g(s-3,p+1) or g(s-4,p+1) or g(s-5,p+1) or g(s//5,p+1)
    else:
        return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1) and g(s - 4, p + 1) and g(s - 5, p + 1) and g(s // 5,p + 1)
for S in range(20,500):
    if g(S,0):
        print(S)


print('№21')
def g(s,p):
    if (p==2 or p==4) and s<=12:
        return 1
    elif p==4 and s>12:
        return 0
    elif p<4 and s<=12:
        return 0
    if p%2 !=0:
        return g(s-1,p+1) or g(s-2,p+1) or g(s-3,p+1) or g(s-4,p+1) or g(s-5,p+1) or g(s//5,p+1)
    else:
        return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1) and g(s - 4, p + 1) and g(s - 5, p + 1) and g(s // 5,p + 1)
for S in range(20,100):
    if g(S,0):
        print(S)