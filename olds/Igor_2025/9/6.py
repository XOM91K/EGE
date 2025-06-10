l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    if len(set(x)) == len(x):
        x.sort()
        if (x[0] + x[-1]) / 2 > sum(x[1:-1]) / 4:
            ct += 1
print(ct)