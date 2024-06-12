l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
ct = 0
for x in l:
    if len(set(x)) == len(x):
        if x[2] * 2 > x[-1] and x[2] * 2 > x[0] * 3:
            ct += 1
print(ct)