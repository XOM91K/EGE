l = [[int(d) for d in x.split()] for x in open('14.txt')]
k = 0
for x in l:
    k += 1
    # [1, 1, 1, 2, 2, 2, 3]
    povt3 = []
    nepovt = 0
    for i in x:
        if x.count(i) == 3:
            povt3.append(i)
    if len(povt3) == 6:
        nepovt = sum(x) - sum(povt3)
        if sum(povt3) / 6 > nepovt:
            print(k)