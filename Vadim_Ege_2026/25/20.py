import fnmatch
def dels(x):
    c = []
    for d in range(2,int(x**0.5)+1):
        if x%d == 0:
            c.append(d)
            c.append(x//d)
    return max(c)-min(c) if len(c) != 0 else 0

c = 0
for x in range(1533878,1,-1):
    b = dels(x)
    if b > 5000 and b%1235 == 0:
        print(x,b)
        c+=1
    if c == 5:
        break

# 1526464 763230
# 1526469 508820
# 1528934 764465
# 1531404 765700
# 1533874 766935