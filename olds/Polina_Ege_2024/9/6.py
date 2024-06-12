l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
k = 0
for x in l:
    k += 1
    povt = []
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(povt) > 0:
        if sum(povt) / len(povt) < sum(x) / len(x):
            print(x, povt)
            ct += k
print(ct)