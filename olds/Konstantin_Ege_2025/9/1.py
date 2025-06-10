l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if x[3] - x[0] >= 50:
        if x[1] * x[2] <= 1000:
            ct += 1
print(ct)