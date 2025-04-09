l = [[int(d) for d in x.split()] for x in open('21.txt')]
k = 0
for x in l:
    k += 1
    c = 0
    c1 = 0
    povt = []
    nepovt = []
    if x.count(x[0]) == 3:
        c += 1
        povt.append(x[0])
    if x.count(x[0]) == 1:
        nepovt.append(x[0])
        c1 += 1
    if x.count(x[1]) == 3:
        c += 1
        povt.append(x[1])
    if x.count(x[1]) == 1:
        nepovt.append(x[1])
        c1 += 1
    if x.count(x[2]) == 3:
        c += 1
        povt.append(x[2])
    if x.count(x[2]) == 1:
        nepovt.append(x[2])
        c1 += 1
    if x.count(x[3]) == 3:
        c += 1
        povt.append(x[3])
    if x.count(x[3]) == 1:
        nepovt.append(x[3])
        c1 += 1
    if x.count(x[4]) == 3:
        c += 1
        povt.append(x[4])
    if x.count(x[4]) == 1:
        nepovt.append(x[4])
        c1 += 1
    if x.count(x[5]) == 3:
        c += 1
        povt.append(x[5])
    if x.count(x[5]) == 1:
        nepovt.append(x[5])
        c1 += 1

    if x.count(x[6]) == 3:
        c += 1
        povt.append(x[6])
    if x.count(x[6]) == 1:
        nepovt.append(x[6])
        c1 += 1

    if c == 6 and c1 == 1:
        povt = set(povt)
        if sum(povt) / len(povt) > sum(nepovt):
            print(k)