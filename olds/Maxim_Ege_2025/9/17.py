l = [[int(d) for d in x.split()] for x in open('17.txt')]
k = 0
for x in l:
    k += 1
    povt3 = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
    nepovt = sum(x) - sum(povt3)
    if len(povt3) == 6:
        if sum(povt3) / len(povt3) > nepovt:
            print(k, x)