l = [[int(d) for d in x.split()] for x in open('1239.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(nepovt) == 3:
        if sum(povt3) ** 2 > sum(nepovt) ** 2:
            ct += 1
print(ct)
