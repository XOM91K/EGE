l =[sorted([int(d) for d in x.split()]) for x in open('11.txt')]
ct = 0
for x in l:
    if ((x[0] + x[5]) / 2) > ((x[1] + x[2] + x[3] + x[4]) / 4):
        if len(set(x)) == 4 and x.count(x[2]) != 3 and x.count(x[3]) != 3:
                ct += 1
print(ct)