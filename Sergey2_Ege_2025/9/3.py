l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    if (x[0] * x[4]) ** 0.5 > (x[1] * x[2] * x[3]) ** (1/3):
        ct += 1
print(ct)