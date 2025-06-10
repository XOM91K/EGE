l =  [sorted([int(d) for d in x.split()]) for x in open('35.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
        if len(povt) == 4 and len(nepovt) == 3:
            if x[0] * x[1] > x[2] + x[3] + x[4] + x[5] + x[6]:
                ct += 1
print(ct)