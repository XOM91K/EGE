l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) > 1]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) > 0 and len(nepovt) > 0:
        if x.count(max(x)) == 1:
            if sum(nepovt) >= sum(povt) * 3:
                ct += 1
print(ct)