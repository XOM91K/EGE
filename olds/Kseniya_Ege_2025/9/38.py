l = [[int(d) for d in x.split()] for x in open('38.txt')]
k = 0
for x in l:
    k += 1
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 6 and len(nepovt) == 1:
        nch = []
        ch = []
        for y in x:
            if y % 2 == 0:
                ch.append(y)
            else:
                nch.append(y)
        if sum(ch) < sum(nch):
            print(k)