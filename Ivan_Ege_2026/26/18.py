kuby = [[int(d) for d in x.split()] for x in open('18.txt')]
kuby = sorted(kuby, key=lambda x: (-x[1], x[0]))
# print(kuby)
ps = []
i = 0
can = True
while len(kuby) != 0:
    if i == len(kuby):
        can = True
        i = 0
    if can:
        ps.append([kuby[0]])
        del kuby[0]
        can = False
        continue
    if abs(kuby[i][1] - ps[-1][-1][-1]) >= 2:
        ps[-1].append(kuby[i])
        del kuby[i]
    else:
        i += 1
print(sum([d[-1] for d in ps[-1]]))
print(sum([d[-1][0] for d in ps]))