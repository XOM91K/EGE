l = [[int(d) for d in x.split()] for x in open('224.txt')]
for x in l:
    if len(set(x)) == 5:
        x.sort()
        if (x[0] + x[-1]) / 2 == (x[1] + x[-2]) / 2 == x[2]:
            print(x)