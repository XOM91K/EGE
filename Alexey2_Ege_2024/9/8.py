l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 3 and len(nepovt) == 4:
        if sum(nepovt) / len(nepovt) <= povt[0]:
            print(x)
            ct += 1
print(ct)