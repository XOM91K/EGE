l = [[int(d) for d in x.split()] for x in open('11.txt')]
k = 0
for x in l:
    k += 1
    ct = [y for y in x if y % 2 == 0]
    nct = [y for y in x if y % 2 != 0]
    if len(ct) == len(nct):
        x = sorted(x)
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[3]:
            print(k)