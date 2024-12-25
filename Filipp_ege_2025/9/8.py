l = [[int(d) for d in x.split()] for x in open('8.txt')]
k = 0
for x in l:
    k += 1
    # [1, 1, 1, 2, 2, 2, 4] => 3
    # [1, 1, 1, 1, 1, 3, 4] => 3
    povt = []
    nepovt = 0
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
        if x.count(y) == 1:
            nepovt = y
    if len(povt) == 6:
        if sum(povt) / 6 < nepovt:
            print(k)

