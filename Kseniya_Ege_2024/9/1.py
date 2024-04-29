l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    # [1, 1, 2, 2, 3, 3, 4]  4
    # [1, 1, 1, 1, 3, 4, 5]
    povt = []
    nepovt = 0
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt = y
    if len(povt) == 6:
        if (max(povt) + min(povt)) / 2 < nepovt:
            ct += 1
print(ct)