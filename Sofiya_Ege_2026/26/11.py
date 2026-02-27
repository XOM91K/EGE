l = [int(x) for x in open('11.txt')]
l = sorted(l, key=lambda d: -d)
can = True
i = 0
blocks = []
while len(l) != 0:
    if i == len(l):
        i = 0
        can = True
    if can:
        blocks.append([l[0]])
        del l[0]
        can = False
    if len(l) == 0:
        break
    if blocks[-1][-1] - l[i] >= 9:
        blocks[-1].append(l[i])
        del l[i]
    else:
        i += 1
print(blocks)
print(len(blocks), len(max(blocks, key=len)))