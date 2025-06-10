l = [sorted([int(d) for d in i.split()]) for i in open('8.txt')]
ct = 0
for i in l:
    if len(i) == len(set(i)):
        if (i[0] + i[-1]) / 2 < (i[1] + i[2] + i[3] + i[4]) / 4:
            ct += 1
print(ct)