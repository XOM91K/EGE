l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    if x[-1]** 2 > x[0] * x[1] * x[2] * x[3]:
        if (x[-1] + x[-2]) > (x[0] + x[1] + x[2]) * 2:
            ct += 1
print(ct)