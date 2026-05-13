l = [int(x) for x in open('7.txt')]
mnch = min([d for d in l if d % 2 == 0])
mnsm = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k == 1:
        if l[x + 1] % mnch == 0:
            mnsm.append(l[x] + l[x + 2])
print(len(mnsm), min(mnsm))