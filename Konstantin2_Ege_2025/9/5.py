l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if (x[0] + x[4]) / 2 == x[2] == (x[1] + x[3]) / 2:
            print(x)