l = [[int(d) for d in x.split()] for x in open('36.txt')]
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
        else:
            nepovt.append(y)
    if len(povt) >= 3:
        sm_kvr = 0
        if len(povt) == 6:
            sm_kvr = povt[0] ** 2 + povt[0] ** 2 + povt[0] ** 2 + povt[0] ** 2 + povt[0] ** 2 + povt[0] ** 2
        if len(povt) == 3:
            sm_kvr = povt[0] ** 2 + povt[0] ** 2 + povt[0] ** 2
        if sm_kvr >= sum(nepovt) ** 2:
            print(sum(x))