l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) == 2]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 4 and len(nepovt) == 3:
        x.sort()
        if x[0] * x[1] > x[2] + x[3] + x[4] + x[5] + x[6]:
            ct +=1
print(ct)