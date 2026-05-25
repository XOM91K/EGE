l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    povt = [d for d in x if x.count(d) > 1]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) > 0 and len(nepovt) > 0:
        x.sort()
        if x.count(x[-1]) == 1:
            if (sum(nepovt) / sum(povt)) >= 3:
                ct += 1
print(ct)