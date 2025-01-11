l = [[int(d) for d in x.split()] for x in open('18.txt')]
k = 0
for x in l:
    k += 1
    # [15, 15, 15, 22, 22, 22, 11] set = 3
    # [15, 11, 22, 22, 22, 22, 22] set = 3
    povt3 = []
    nepovt = 0
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
    nepovt = sum(x) - sum(povt3)
    if len(povt3) == 6:
        if sum(povt3) / len(povt3) > nepovt:
            print(k)