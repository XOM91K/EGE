l = sorted([int(x) for x in open('6.txt')])[::-1]
blocks = []
print(l)
j = 0
can = True
while len(l) != 0:
    if can:
        blocks.append([l[0]])
        del l[0]
        can = False
        if len(l) == 0:
            break
    if blocks[-1][-1] - l[j] >= 9:
        blocks[-1].append(l[j])
        del l[j]
    else:
        j += 1
    if j == len(l):
        can = True
        j = 0
print(blocks)
print(len(blocks), len(max(blocks, key=len)))