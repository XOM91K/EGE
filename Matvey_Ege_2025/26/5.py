l = [int(x) for x in open('5.txt')]
l = sorted(l)[::-1]
k = 9
blocks = []
can = True
j = 0
while len(l) > 0:
    if j == len(l):
        can = True
        j = 0
    if can:
        blocks.append([l[0]])
        del l[0]
        can = False
    else:
        if blocks[-1][-1] - l[j] >= k:
            blocks[-1].append(l[j])
            del l[j]
        else:
            j += 1

print(len(blocks), len(max(blocks, key=len)))