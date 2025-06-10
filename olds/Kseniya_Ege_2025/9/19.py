l = [sorted([int(d) for d in x.split()]) for x in open('19.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        ch = []
        nch = []
        for y in x:
            if y % 2 == 0:
                ch.append(y)
            else:
                nch.append(y)
        if len(nch) > len(ch): #чезабретта
            if sum(nch) < sum(ch):
                ct += 1
print(ct)