l = [[int(d) for d in x.split()] for x in open('16.txt')]
k = 0
for x in l:
    k += 1
    povt2 = []
    povt3 = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 2:
            povt2.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt3) == 3 and len(povt2) == 2 and len(nepovt) == 3:
        if povt3[0] > povt2[0]:
            print(k)