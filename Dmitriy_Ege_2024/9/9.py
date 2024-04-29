l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    ch = []
    nch = []
    if len(set(x)) == len(x):
        for y in x:
            if y % 2 == 0:
                ch.append(y)
            else:
                nch.append(y)
        if len(ch) < len(nch):
            if sum(ch) > sum(nch):
                ct += 1
print(ct)