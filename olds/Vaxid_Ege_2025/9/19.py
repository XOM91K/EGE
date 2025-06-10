l = [[int(d) for d in x.split()] for x in open('19.txt')]
sp = [[], [], [], [], [], []]
for x in l:
    sp[0].append(x[0])
    sp[1].append(x[1])
    sp[2].append(x[2])
    sp[3].append(x[3])
    sp[4].append(x[4])
    sp[5].append(x[5])
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt) == 3:
        k = 0
        if sp[0].count(povt[0]) == 337:
            k += 1
        if sp[5].count(nepovt[0]) == 337 or sp[5].count(nepovt[1]) == 337 or sp[5].count(nepovt[2]) == 337:
            k += 1
        if k > 0:
            ct += 1
print(ct)