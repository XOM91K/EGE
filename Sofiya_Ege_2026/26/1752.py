l=[x for x in open('1752.txt')]
yach=[[int(d) for d in x.split()]for x in l[:200]]
yach=sorted(yach, key=lambda d: d[-1])
print(yach)
for x in yach:
    x.extend([0, 0, 0])
print(yach)
#номер цена занято
tovar=[[int(d)for d in x.split()]for x in l[200:]]
tovar=sorted(tovar, key=lambda d: d[0])
print(tovar)
#нач кон
for x in tovar:
    for y in range(len(yach)):
            if x[0] > yach[y][-1]:
                yach[y][-1] = x[1]
                yach[y][2] += (yach[y][1]*(x[-1]-x[0]+1))
                yach[y][3] += 1
                break
print(sorted(yach, key=lambda d: d[2])[::-1])