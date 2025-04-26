l = [[int(d) for d in x.split()] for x in open('17.txt')]
k = 0
for x in l:
    k += 1
    ch = [y for y in x if y % 2 == 0]
    nch = [y for y in x if y % 2 != 0]
    if len(ch) == len(nch):
        x.sort()
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[-3]:
            print(k, x)