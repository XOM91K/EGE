l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
ct = 0
for x in l:
    if x[0] < 180 or x[1] < 180 or x[2] < 180 or x[3] < 180:
        if x[0] + x[1] + x[2] + x[3] == 360:
            ct += 1
print(ct)