l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if x[2] * 2 > x[-1] and x[2] * 2 > 3 * x[0]:
            print(x)
            ct += 1
print(ct)