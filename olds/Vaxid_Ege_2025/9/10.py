l = [[int(d) for d in x.split()] for x in open('10.txt')]
k = 0
for x in l:
    k += 1
    #  [22, 22, 22, 43, 43, 43, 7] set => 3
    #  [22, 22, 22, 22, 22, 3, 7] set => 3
    #  [22, 22, 22, 43, 43, 23, 23] set => 3
    povt3 = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt3) == 6:
        if sum(povt3) / 6 > nepovt[0]:
            print(k)