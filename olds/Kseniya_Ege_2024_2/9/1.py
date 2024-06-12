l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    if x[0] != min(x) and x[0] != max(x) and x[3] != min(x) and x[3] != max(x):
        r = sorted(x.copy())
        if (r[2] - r[1]) != 0 and (max(x) - min(x)) % (r[2] - r[1]) == 0:
            ct += 1
print(ct)