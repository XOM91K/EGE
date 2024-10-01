l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        povt = []
        for y in x:
            if x.count(y) > 1:
                povt.append(y)
        if len(povt) > 0:
            if x[0] + x[-1] < sum(povt):
                ct += 1
print(ct)