l = [[int(d) for d in x.split()] for x in open('14.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    k = 0
    if len(povt) == 3 and len(nepovt) == 4:
        k += 1
    if x == sorted(x):
        k += 1
    if k < 2:
        ct += 1
print(ct)