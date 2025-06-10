l = [[int(d) for d in x.split()] for x in open('33.txt')]
k = 0
for x in l:
    k += 1
    ch  = []
    nch = []
    for y in x:
        if y % 2 == 0:
            ch.append(y)
        else:
            nch.append(y)
    if len(ch) == len(nch):
        x = sorted(x)
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[3]:
            print(k, x)