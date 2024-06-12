import collections
l = [int(x) for x in open('6.txt')]
sm = ct = sr = ct_tr = 0
for x in l:
    if x % 17 == 0:
        sm += x
        ct += 1
sr = sm / ct
g = []
for x in range(len(l) - 2):
    if len(str(l[x])) == 4 and len(str(l[x + 1])) == 4 and len(str(l[x + 2])) == 4:
        sm1 = str(l[x])
        sm1 = int(sm1[0]) + int(sm1[1]) + int(sm1[2]) + int(sm1[3])
        sm2 = str(l[x + 2])
        sm2 = int(sm2[0]) + int(sm2[1]) + int(sm2[2]) + int(sm2[3])
        smsr = str(l[x + 1])
        smsr = int(smsr[0]) + int(smsr[1]) + int(smsr[2]) + int(smsr[3])
        if sm1 == sm2 and l[x + 1] < sr:
            g.append(smsr)
            ct_tr += 1
print(ct_tr)
print(collections.Counter(g))