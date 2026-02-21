l = [int(x) for x in open('5.txt')]
l = sorted(l)[::-1]
# (55, 38, 18, 2), (48, 16), (47)
i = 1
can = True
blocks = []
while len(l) != 0:
    if can:
        blocks.append([l[0]])
        del l[0]
        can = False
        if len(l) == 0:
            break
    if blocks[-1][-1] - l[i] >= 9:
        blocks[-1].append(l[i])
        del l[i]
        if i == len(l):
            i = 0
            can = True
    else:
        i += 1
        if i == len(l):
            i = 0
            can = True
print(len(blocks), len(max(blocks, key=len)))