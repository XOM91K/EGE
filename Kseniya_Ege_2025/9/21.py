l = [[int(d) for d in x.split()] for x in open('21.txt')]
n = 0
for x in l:
    n += 1
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 6:
        if sum(povt) / 6 > nepovt[0]:
            print(n, x)