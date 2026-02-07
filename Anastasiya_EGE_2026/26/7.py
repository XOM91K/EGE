k = 9
l = [int(x) for x in open('7.txt')]
l = sorted(l)[::-1]
blocks = []
can = True
i = 0
while len(l) > 0:
    if can:
        blocks.append([l[0]])
        can = False
        del l[0]
    elif blocks[-1][-1] - l[i] >= k:
        blocks[-1].append(l[i])
        del l[i]
    else:
        i += 1
    if i == len(l):
        can = True
        i = 0
print(len(blocks), len(max(blocks, key=len)))