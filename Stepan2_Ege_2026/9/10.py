l = [[int(d) for d in x.split()] for x in open('10.txt')]
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt1) == 5:
        x = sorted(x)
        if (x[0] + x[-1]) / 2 == x[2] == (x[1] + x[-2]) / 2:
            print(x)