d = 9
l = sorted([int(x) for x in open('8.txt')])[::-1]
bloks = []
i = 0
can = True
while len(l) != 0:
    if i == len(l):
        can = True
        i = 0
    if can:
        bloks.append([l[i]])
        del l[i]
        can = False
    else:
        if abs(bloks[-1][-1] - l[i]) >= d:
            bloks[-1].append(l[i])
            del l[i]
        else:
            i += 1
print(len(bloks), len(max(bloks, key=len)))