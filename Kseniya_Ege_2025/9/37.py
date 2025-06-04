l = [sorted([int(d) for d in x.split(',')]) for x in open('37.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        if (x[-2] + x[-1]) * 2 >= (x[0] + x[1] + x[2] + x[3]) * 3:
            ct += 1
print(ct)