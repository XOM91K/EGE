l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x[0] != x[1]:
        if len(set(x)) < 6:
            povt = []
            for y in x:
                if x.count(y) > 1:
                    povt.append(y)
            if x[-1] + x[0] < sum(povt):
                ct += 1
print(ct)