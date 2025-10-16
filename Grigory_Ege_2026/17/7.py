l = [int(d) for d in open('7.txt')]
ms = []
k32 = len([y for y in l if y % 32 == 0])
for x in range(len(l) - 1):
    k = 0
    if l[x] < 0  or l[x + 1] < 0 :
        if l[x]+l[x+1] < k32:
            ms.append(l[x]+l[x+1])
print(len(ms),max(ms))