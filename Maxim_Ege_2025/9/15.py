l = [[int(d) for d in x.split()] for x in open('15.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 4 and len(nepovt) == 2:
        if max(povt) ** 2 > nepovt[0] * nepovt[1]:
            ct += 1
            print(x, povt, nepovt, max(povt))
print(ct)
# [22, 22, 11, 11, 9, 8] 4
# [1, 1, 1, 3, 4, 5] 4
