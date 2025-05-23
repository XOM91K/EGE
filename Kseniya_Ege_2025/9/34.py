l =  [sorted([int(d) for d in x.split()]) for x in open('34.txt')]
n = 0
for x in l:
    n += 1
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 6 and len(nepovt) == 2:
        if (max(povt) - min(povt)) ** 2 > (nepovt[0] ** 2 + nepovt[1] ** 2) * 2:
            print(n)