l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for x1 in x:
        if x.count(x1) > 1:
            povt.append(x1)
        else:
            nepovt.append(x1)
    if len(povt) == 2 and sum(nepovt) / len(nepovt) <= sum(povt):
        ct += 1
print(ct)