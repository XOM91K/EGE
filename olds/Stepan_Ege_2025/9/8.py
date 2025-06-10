l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    povt3 = []
    nepovt = []
    for y in range(0, 6):
        if x.count(x[y]) == 3:
            povt3.append(x[y])
        elif x.count(x[y]) == 1:
            nepovt.append(x[y])
    if len(povt3) == 3 and len(nepovt) == 3:
        if sum(nepovt) / 3 < sum(povt3):
            ct += 1
print(ct)