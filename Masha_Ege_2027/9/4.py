l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    povt2 = [y for y in x if x.count(y) == 2]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt2) == 4:
        if max(povt2) ** 2 > povt1[0] * povt1[1]:
            ct += 1
print(ct)