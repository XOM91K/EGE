l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt1) == 7:
        x = sorted(x)
        if x[0] * x[1] <= x[2] + x[3] + x[4] + x[5] + x[6]:
            ct += 1
            print(x)
print(ct)