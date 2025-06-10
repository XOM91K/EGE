l = [sorted([int(d) for d in x.split()]) for x in open('18.txt')]
q = 0
for x in l:
    q += 1
    # [1, 1, 1, 2, 2, 2, 7]
    k = 0
    if x.count(x[0]) == 3:
        k += 1
    if x.count(x[1]) == 3:
        k += 1
    if x.count(x[2]) == 3:
        k += 1
    if x.count(x[3]) == 3:
        k += 1
    if x.count(x[4]) == 3:
        k += 1
    if x.count(x[5]) == 3:
        k += 1
    if x.count(x[6]) == 3:
        k += 1
    if k == 6:
        povt = []
        nepovt = []
        if x.count(x[0]) == 3:
            povt.append(x[0])
        else:
            nepovt.append(x[0])
        if x.count(x[1]) == 3:
            povt.append(x[1])
        else:
            nepovt.append(x[0])
        if x.count(x[2]) == 3:
            povt.append(x[2])
        else:
            nepovt.append(x[0])
        if x.count(x[3]) == 3:
            povt.append(x[3])
        else:
            nepovt.append(x[0])
        if x.count(x[4]) == 3:
            povt.append(x[4])
        else:
            nepovt.append(x[0])
        if x.count(x[5]) == 3:
            povt.append(x[5])
        else:
            nepovt.append(x[0])
        if x.count(x[6]) == 3:
            povt.append(x[6])
        else:
            nepovt.append(x[6])
        if sum(povt) / 6 > nepovt[0]:
            print(q)