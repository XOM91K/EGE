l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
            #povt [1,1,5,5]
            #nepovt [10]
    if len(povt) == 4:
        if povt[1] < nepovt[0] < povt[3]:
            ct += 1
print(ct)
