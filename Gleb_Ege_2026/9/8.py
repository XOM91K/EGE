l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    if len(set(x)) == 3:
        x.sort()
        if (x[-1] + x[-2]) / (x[0] + x[1]) > 2 and (x[-1] % x[0]) != 0:
            ct += 1
            print(x)
print(ct)