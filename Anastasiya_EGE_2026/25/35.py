import math
def dels(n):
    s=[]
    for x in range(1,int(n**0.5)+1):
        if n%x==0:
            s.append(x)
            s.append(n//x)
    return sorted(set(s))
for y in range(800_001, 10 ** 7):
    d=dels(y)
    if len(d)>10:
        if sum(d)%2!=0 and math.prod(d) % 2 != 0:
            print(y, len(d))