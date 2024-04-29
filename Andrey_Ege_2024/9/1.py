l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if abs((x[-1]-x[0])**3) <= (x[1] + x[2]) ** 2:
        ct += 1
print(ct)