ct=0
def v49(n):
    s=[]
    while n > 0 :
        s.append(n%49)
        n//=49
    return s[::-1]
d=15*2401**1500-10*343**1200+40*49**1000-35*7**850-4805
r=v49(d)
for i in  r:
    if i>9:
        ct+=1
print(ct)
