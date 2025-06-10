import math
l = [[int(d) for d in x.split()] for x in open('22.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 4 and len(nepovt) == 2:
        if (max(povt) ** 2) > math.prod(nepovt):
            ct += 1
print(ct)