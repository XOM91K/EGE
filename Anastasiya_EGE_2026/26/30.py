l = [[int(d) for d in x.split()] for x in open('30.txt')]
l = sorted(l, key=lambda d: -d[1])
bashni = []
can = True
i = 0
while len(l) > 0:
    if i == len(l):
        can = True
        i = 0
    if can:
        bashni.append([l[0]])
        del l[0]
        can = False
    else:
        if bashni[-1][-1][-1] - l[i][1] >= 2:
            bashni[-1].append(l[i])
            del l[i]
        else:
            i += 1
print([len(d) for d in bashni])
print(bashni[-1][0][-1] + bashni[-1][1][-1] + bashni[-1][2][-1])
print(sum([d[-1][0] for d in bashni]))