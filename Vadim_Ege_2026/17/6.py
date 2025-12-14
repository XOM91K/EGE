l = [int(x) for x in open("6.txt")]
d = max([x for x in l if len(str(abs(x)))==5 and abs(x)%10 == 3]) ** 2
m = []
for x in range(0,len(l)-2):
    k = 0
    if len(str(abs(l[x]))) == 5 and abs(l[x])%10==3:
        k+=1
    if len(str(abs(l[x+1]))) == 5  and abs(l[x+1])%10==3:
        k+=1
    if len(str(abs(l[x+2]))) == 5  and abs(l[x+2])%10==3:
        k+=1
    if k >= 2 and l[x]**2+l[x+1]**2+l[x+2]**2 <= d:
      m.append(l[x]**2+l[x+1]**2+l[x+2]**2)
print(len(m),min(m))