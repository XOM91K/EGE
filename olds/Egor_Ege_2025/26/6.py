l = [int(x) for x in open('6.txt')]
l = sorted(l)[::-1]
blocks = []
while len(l) > 0:
    i = 0
    blocks.append([l[0]])
    del l[0]
    while i < len(l):
        if blocks[-1][-1] - l[i] >= 9:
            blocks[-1].append(l[i])
            del l[i]
        else:
            i += 1
print(len(blocks), len(max(blocks, key=len)))