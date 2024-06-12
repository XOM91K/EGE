l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
k = 0
for x in l:
    povt = []
    k += 1
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(povt) > 0 and (sum(povt) / len(povt)) < (sum(x) / len(x)):
        ct += k
print(ct)