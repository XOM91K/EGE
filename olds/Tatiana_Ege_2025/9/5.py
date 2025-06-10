c = 0
l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
for i in l:
    if i.count(i[0]) == 1 and len(set(i)) < len(i) and i[0] + i[5] < ((i[1] + i[2] + i[3] + i[4]) / 4) * 2:
        c += 1
print(c)