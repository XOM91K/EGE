l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
i = 0
for x in l:
    i += 1
    povt3 = [y for y in x if x.count(y) == 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 6:
        if sum(povt3) / 6 < povt1[0]:
            ct += 1
            print(x, i)
print(ct)
#print([3, 2, 1] - [2, 1])