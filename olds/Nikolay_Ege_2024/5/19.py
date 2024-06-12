l = [sorted(int(d) for d in x.split()) for x in open('19.txt'
                                                     '')]
# print(l)
ct = 0
for x in l:
    k = 0
    povt3 = []
    nepovt = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if (x[0] + x[-1]) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2:
        k += 1
    if len(nepovt) == 3 and len(povt3) == 3:
        k += 1
    if k >=1:
        ct += 1
print(ct, x)