l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if x[2] * 2 > x[-1] and x[2] * 2 > x[0] * 3:
            ct += 1
print(ct)