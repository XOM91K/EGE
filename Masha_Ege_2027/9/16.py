l = [[int(d) for d in x.split()] for x in open('16.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        x = sorted(x)
        if (x[0] + x[-1]) / 2 > sum(x[1:-1]) / 4:
            print(x)
            ct += 1
print(ct)