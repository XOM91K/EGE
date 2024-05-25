l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for i in x:
        if x.count(i) == 3:
            povt.append(i)
        elif x.count(i) == 1:
            nepovt.append(i)
    mx = max(x)
    mn = min(x)
    x.remove(max(x))
    x.remove(min(x))
    if ((mx + mn) ** 2) > (x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2) or (len(povt) == 3 and len(nepovt) == 3):
            ct += 1
print(ct)