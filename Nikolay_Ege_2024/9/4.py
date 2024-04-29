l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = -1
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt = y
    if len(povt) == 4:
        if min(povt) <= nepovt <= max(povt):
            ct += 1
print(ct)
