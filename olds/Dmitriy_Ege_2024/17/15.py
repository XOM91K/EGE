l = [int(x) for x in open('15.txt')]
sm = []
ct = 0
mn = []
for x in l:
    mn.append(x)
mn = sorted(mn)
mn.pop(-1)
mn.pop(-1)
print(max(mn))

for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k != 3 and (l[x] + l[x + 1] + l[x + 2]) <= max(mn):
            ct += 1
            sm.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(sm))