l = [sorted([int(d) for d in x.split(',')]) for x in open('19.txt')]
ct = 0
for x in l:
    if len(x) == len(set(x)):
        if (x[5] + x[4]) * 2 >= (x[0] + x[1] + x[2] + x[3]) * 3:
            ct += 1
            print(ct, x)