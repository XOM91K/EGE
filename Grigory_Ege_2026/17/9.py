l=[ int(d) for d in open('9.txt')]
ar = [y for y in l if abs(y) % 100 == 28]
ar = sum(ar) / len(ar)
ms = []
for x in range(len(l) - 2):
    if len(str(abs(l[x])))==4 or len(str(abs(l[x+1])))==4 or len(str(abs(l[x+2])))==4:
        k = 0
        if abs(l[x])%100 == 11:
            k+=1
        if abs(l[x+1])%100 == 11:
            k+=1
        if abs(l[x+2])%100 == 11:
            k+=1
        if k == 2:
            if l[x]>ar and l[x+1]>ar and l[x+2]>ar :
                ms.append(l[x]+l[x+1]+l[x+2])
print(len(ms),min(ms))
# print(100 % 28)
# print(-100 % 28)