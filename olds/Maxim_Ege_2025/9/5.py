l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    povt = []
    x.sort()
    if x.count(x[0]) == 1:
        for y in x[1:]:
            if x.count(y) > 1:
                povt.append(y)
        if len(povt) > 0:
            if x[-1] + x[0] < sum(povt):
                ct += 1
print(ct)