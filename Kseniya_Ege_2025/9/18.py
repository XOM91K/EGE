l = [sorted([int(d) for d in x.split()]) for x in open('18.txt')]
ct = 0
for x in l:
    if x[-1] < (x[0] + x[1] + x[2]):
        ch = []
        nch = []
        # [100, 50, 25, 100]
        for y in x:
            if y % 2 == 0:
                ch.append(y)
            else:
                nch.append(y)
        if sum(ch) == sum(nch):
            ct+= 1
print(ct)