l = [[int(d) for d in x.split()] for x in open('14.txt')]
ct = 0
for x in l:
    povt3 = []
    povt2 = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 2:
            povt2.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt3) == 3 and len(povt2) == 2 and len(nepovt) == 3:
        if sum(nepovt) / len(nepovt) <= povt3[0]:
            ct += 1
print(ct)