l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    # [1, 1, 2, 2, 3, 3, 5]
    povt = []
    nepovt = 0
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt = y
    if len(povt) == 6:
        if (min(povt) + max(povt)) / 2 < nepovt:
            ct += 1
print(ct)