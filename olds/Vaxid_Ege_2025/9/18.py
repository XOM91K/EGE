l = [[int(d) for d in x.split()] for x in open('18.txt')]
for x in l:
    if x == sorted(x)[::-1]:
        if (x[-1] + x[0]) / 2 > (x[1] + x[2] + x[3] + x[4] + x[5]) / 5:
            print(x, sum(x))