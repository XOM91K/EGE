l = [int(x) for x in open('9.txt')]
l = sorted(l, reverse=True)
blocks = []
while len(l) > 0:
    blocks.append([l[0]])
    del l[0]
    j = 0
    while j != len(l):
        if blocks[-1][-1] - l[j] >= 9:
            blocks[-1].append(l[j])
            del l[j]
            j -= 1
        j += 1

print(len(blocks), len(max(blocks, key=len)))