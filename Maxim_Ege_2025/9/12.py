l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    x.sort()
    if len(set(x)) == 4 and (x.count(x[2]) != 3 and x.count(x[3]) != 3):
        print(x)
        if (x[0] + x[-1]) / 2 < (x[1] + x[2] + x[3] + x[4]) / 4:
            ct += 1
print(ct)