l = [[int(d) for d in x.split()] for x in open('949.txt')]
ct = 0
# 22 22 44 44 1 2
for x in l:
    povt2 = [y for y in x if x.count(y) == 2]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt2) == 4 and len(nepovt) == 2:
        if sum(set(povt2)) < sum(nepovt):
            ct += 1
print(ct)